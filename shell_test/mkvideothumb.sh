:
##########################################################################
# Title      :  mkvideothumb - create animated GIF as a preview for a video
# Author     :  Heiner Steven <heiner.steven@odn.de>
# Date       :  2015-04-13
# Category   :  Video
# Requires   :  convert, ffmpeg, showvideoduration
# SCCS-Id.   :  @(#) mkvideothumb   1.2 18/05/03
##########################################################################
# Description
#
# TODO
##########################################################################

PN=`basename "$0"`          # Program name
VER='1.2'

set -u

: ${PREVIEW_IMAGE_COUNT:=20}
: ${DEFAULT_FRAME_DELAY=1/1}

WorkDir=${TMPDIR:=/tmp}/$PN.$$
Logfile=$WorkDir/$PN-$$.log
PublicLog=$TMPDIR/$PN.log

usage () {
    echo >&2 "$PN - create animated GIF as a preview for a video, $VER
usage: $PN [-hf] [{-d delay | -r rate}] [-n imgcnt] [-s size] \
    [-o outfile] video [...]
   -d   delay (in seconds) between each frame (default: $DEFAULT_FRAME_DELAY).
        Use a quotient for specifying parts of a second, e.g. 1/2 for 0.5s.
   -r   (rate) images per second to show
   -f   overwrite existing files; continue after errors (default: false)
   -n   number of preview images to extract  (default: $PREVIEW_IMAGE_COUNT)
   -o   output file name (must end with '.gif'). Default: input file name with
        '.gif' extension)
   -s   video frame size (width x height, default: same as video)
   -h:  print this usage summary"
    exit 1
}

msg () { echo >&2 "$PN:" "$@";  }

fatal () { msg "$@"; exit 1; }

tmpimgext=.jpg
tmpimgfmt="frame_%05d${tmpimgext}"

##########################################################################
# extract_thumb_images - extract sample images from the video stream
##########################################################################

extract_thumb_images () {
    [ $# -eq 1 ] || fatal "usage: extract_thumb_images inputfile"

    : ${WorkDir?} ${Logfile?}
    : ${rate?} ${tmpimgfmt?}
    : ${filenum?}
    : ${framewidth?} ${frameheight?}

    #_prefix=`basename "$1"`
    _prefix="file_`echo "00000$filenum" | sed 's/^.*\(.....\)$/\1/'`"

    if [ -n "${framewidth}${frameheight}" ]
    then scalearg="-s ${framewidth}x${frameheight}"
    else scalearg=
    fi

    set -x
    ffmpeg -y -i "$1" -r $rate $scalearg "$WorkDir/${_prefix}_$tmpimgfmt" \
        >> "$Logfile" 2>&1
    _error=$?
    set +x
    unset _prefix

    return $_error
}

##########################################################################
# create_thumb - combine sample images to an animated GIF image
##########################################################################

create_thumb () {
    [ $# -eq 1 ] || fatal "usage: create_thumb outputfile"

    : ${WorkDir?} ${Logfile?}
    : ${tmpimgext?}

    # Write to temporary file
    _tmpdir=`dirname "$1"`
    _tmpbase=`basename "$1"`
    _tmpfile=$_tmpdir/.$$.${_tmpbase}

    _delayarg=
    [ -n "$frame_delay" ] && _delayarg="-delay ${frame_delay}"
    [ -n "$frame_rate" ]  && _delayarg="-delay 1x${frame_rate}"

    set -x
    convert -fuzz 1% +dither $_delayarg "$WorkDir/*$tmpimgext" -coalesce \
            -layers OptimizeTransparency "$_tmpfile" >> "$Logfile" 2>&1
    set +x

    if [ $_error -eq 0 ] && [ -s "$_tmpfile" ] && mv -f -- "$_tmpfile" "$1"
    then
    _error=0
    else
    _error=1
    rm -f -- "$_tmpfile"
    fi

    unset _tmpdir _tmpbase _tmpfile _delayarg

    delete_tempfiles

    return $_error
}

##########################################################################

delete_tempfiles () {
    : ${WorkDir?} ${tmpimgext?}
    #set -x
    rm -f "$WorkDir/"*"$tmpimgext"
    #set +x
}

##########################################################################

is_valid_integer ()
{
    [ $# -eq 1 ] || fatal "usage: $0 string"

    case "$1" in
    *[!0-9]*)   return 1;;
    *)      return 0;;
    esac
}

parse_duration ()
{
    [ $# -eq 1 ] || fatal "usage: $0 string"

    if is_valid_integer "$1"
    then
        echo "$1"
    return 0
    else
    # Format: seconds[/divisor]
    set -- `echo "$1" |
        sed 's/[    ]//g' |
        awk '
        # Examples: "640x480", "x640", "640x"
        /^[0-9][0-9]*\/[0-9][0-9]*$/ ||
            /^\/[0-9][0-9]*$/ ||
            /^[0-9][0-9]*\/$/ {
            split($0, f, /\//)
            print f[1] + 0, f[2] + 0
        }
        '
    `
    if [ $# -eq 2 ]
    then
        echo "${1}x${2}"
        return 0
    fi
    fi

    return 1
}

##########################################################################

parse_frame_size () {
    [ $# -eq 1 ] || fatal "usage: parse_frame_size argument"

    # Format: width[x height]
    set -- `echo "$1" |
    sed 's/[    ]//g' |
    awk '
        # Examples: "640x480", "x640", "640x"
        /^[0-9][0-9]*x[0-9][0-9]*$/ ||
            /^x[0-9][0-9]*$/ ||
            /^[0-9][0-9]*x$/ {
            split($0, f, /x/)
        print f[1] + 0, f[2] + 0
        }
    '
    `
    if [ $# -eq 2 ]
    then
    FrameWidth=$1
    FrameHeight=$2
    return 0
    fi

    return 1
}

##########################################################################

FrameDelay=
FrameRate=
PreviewImageCount=
ForceRun=false
Output=
while getopts :d:fhn:o:r:s: opt
do
    case "$opt" in
    d)
        FrameDelay=`parse_duration "$OPTARG"`
        [ -n "$FrameDelay" ] ||
        fatal "ERROR: invalid frame delay: $OPTARG"
        ;;
    f)  ForceRun=true;;
    h)  usage;;
    n)
        if is_valid_integer "$OPTARG"
        then PreviewImageCount=$OPTARG
        else
        fatal "ERROR: invalid number of images: $OPTARG"
        fi
        ;;
    o)  Output=$OPTARG;;
    r)
        if is_valid_integer "$OPTARG"
        then FrameRate=$OPTARG
        else
        fatal "ERROR: invalid frame rate: $OPTARG"
        fi
        ;;
    s)              # Set FrameWidth and FrameHeight
        if parse_frame_size "$OPTARG"
        then : ${FrameWidth?} ${FrameHeight?}
        else
        fatal "ERROR: invalid frame size: $OPTARG"
        fi
        ;;
    ?)  usage;;
    esac
done
shift `expr ${OPTIND-1} - 1`

[ $# -lt 1 ] && usage

if [ -n "$FrameDelay" ] && [ -n "$FrameRate" ]
then
    msg "ERROR: options -d and -r are mutually exclusive"
    fatal "($PN -h prints a usage message)"
fi

preview_image_count=${PreviewImageCount:-$PREVIEW_IMAGE_COUNT}
frame_delay=${FrameDelay:=`parse_duration "$DEFAULT_FRAME_DELAY}"`}
frame_rate=${FrameRate:-}
framewidth=${FrameWidth:-}
frameheight=${FrameHeight:-}

if [ -n "$Output" ] && [ $# -gt 1 ]
then combine_images=true
else combine_images=false
fi

#msg "DEBUG: ${frame_delay:+delay ${frame_delay}s after each image} ${frame_rate:+animation speed $frame_rate images/s} ${framewidth:+size ${framewidth}x$frameheight}"

##########################################################################

if mkdir "$WorkDir"
then
    trap 'rm -rf "$WorkDir" >&2' 0
    trap "exit 1" 1 2 3 13 15
else
    fatal "ERROR: cannot create temporary directory '$WorkDir'"
fi

error=0
filenum=0       # File number, used as part of temporary file name
for videofile
do
    filenum=`expr $filenum + 1`
    errormsg=

    [ -f "$videofile" ] || : ${errormsg:="cannot read file '$videofile'"}
    [ -s "$videofile" ] || : ${errormsg:="file '$videofile' is empty"}

    if [ -z "$errormsg" ]
    then
    # Result file name
    thumbfile=${Output:-`echo "$videofile" | sed 's/\.[^.]*$/.gif/'`}
    if [ -f "$thumbfile" ] && [ -s "$thumbfile" ] &&
        [ "$ForceRun" != "true" ]

    then
        msg "WARNING: will not overwrite existing file '$thumbfile'.
Use option -f for overwriting existing result files."
        continue
    fi
    fi

    if [ -z "$errormsg" ]
    then
    durationtxt=`showvideoduration -s "$videofile"`
    duration=`echo "$durationtxt" | awk '{print $1 + 0}'`
    if [ -z "$durationtxt" ] || [ "$duration" = "0" ] &&
        [ "$ForceRun" != "true" ]
    then
        errormsg="\
cannot determine length of video
        '$videofile'
This usually means that the input file is not valid video file.
If you want to process it nevertheless, use option -f."
    fi
    fi

    if [ -z "$errormsg" ]
    then
    rate=`awk '
        BEGIN {
        imagecount = '"$preview_image_count"' + 0
        duration = '"$duration"' + 0
        if (duration < imagecount) duration = 1
        print imagecount / duration
        }
        '`

    msg "DEBUG: $videofile; duration=$duration rate=$rate"

    : ${rate:=$preview_image_count}

    if extract_thumb_images "$videofile"
    then
        if [ "$combine_images" != "true" ]
        then
        if create_thumb "$thumbfile"
        then msg "INFO: wrote file '$thumbfile'"
        else errormsg="cannot create thumb file '$thumbfile'"
        fi
        fi
    else
        errormsg="cannot extract thumb images from stream '$videofile'"
    fi
    fi

    if [ -n "$errormsg" ]
    then
    if [ "$ForceRun" != "true" ]
    then
        msg "ERROR: $errormsg"
        error=1
        break
    else
        msg "WARNING: $errormsg - ignored"
    fi
    fi
done

if [ "$error" = "0" ] && $combine_images
then
    if create_thumb "$thumbfile" 
    then
    msg "INFO: wrote thumb file '$thumbfile'"
    else
    msg "ERROR: cannot create thumb file '$thumbfile'"
    error=1
    fi
fi

if [ "$error" != "0" ] && [ -s "$Logfile" ]
then
    cp -f "$Logfile" "$PublicLog"
    msg "NOTE: the following file contains log messages: $PublicLog"
fi

exit $error

##########################################################################
#ffmpeg -i "$videofile" -r $rate -vf scale=480:-1 "$WorkDir/frame_%04d.png"
#ffmpeg -i "$videofile" -r $rate "$WorkDir/frame_%05d.jpg"
##ffmpeg -i "$videofile" -t 60 -r 10000 -vf scale=480:-1 "$WorkDir/thumb.gif"
#ffmpeg -y -loop 1 -r 1 -i "$WorkDir/frame_%04d.png" -c:v libx264 -r 30 -pix_fmt yuv420p "$WorkDir/slideshow.mp4"
##ffmpeg -y -r 1/1 -i "$WorkDir/frame_%05d.jpg" -vcodec libx264 "$WorkDir/slideshow.mp4"
#convert -fuzz 1% +dither -delay 1x1 "$WorkDir/*.jpg" -coalesce -layers OptimizeTransparency "$WorkDir/animation.gif"
