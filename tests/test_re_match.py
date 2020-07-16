import unittest
import re


class TestReMatch(unittest.TestCase):

    def test_some_case(self):
        s = """<img '
'onload="this.parentNode.parentNode.classList.remove(\'placeholder\')" '
'class="" alt="" '
'data-src="https://images.weserv.nl/?url=https://i.imgur.com/kewGjoO.jpg#vwid=860&vhei=1290" '
'src="https://images.weserv.nl/?url=https://i.imgur.com/kewGjoO.jpg#vwid=860&vhei=1290"></a></figure><br><figure '
'class="placeholder size-parsed" style="flex-grow: 33.884948778566" ><a '
'style="padding-top: 147.55813953488%" no-pjax data-fancybox="gallery" '
'data-caption="" '
'href="https://images.weserv.nl/?url=https://i.imgur.com/4bLkVbY.jpg#vwid=860&vhei=1269">

<img '
'onload="this.parentNode.parentNode.classList.remove(\'placeholder\')" '
'class="" alt="" '
'data-src="https://images.weserv.nl/?url=https://i.imgur.com/4bLkVbY.jpg#vwid=860&vhei=1269" '
'src="https://images.weserv.nl/?url=https://i.imgur.com/4bLkVbY.jpg#vwid=860&vhei=1269"></a></figure><br><figure '
'class="placeholder size-parsed" style="flex-grow: 37.423846823325" ><a '
'style="padding-top: 133.60465116279%" no-pjax data-fancybox="gallery" '
'data-caption="" '
'href="https://images.weserv.nl/?url=https://i.imgur.com/0UAtXIp.jpg#vwid=860&vhei=1149">
"""
        p = re.compile(
            #"https://images.weserv.nl/\?url=https://i.imgur.com/\w*.jpg"
            "http.*\#vwid"
        )
        tempList = re.findall(p, s)
        print(tempList)


if __name__ == '__main__':
    unittest.main()
