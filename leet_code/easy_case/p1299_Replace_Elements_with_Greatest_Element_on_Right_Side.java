class Solution {
    public int[] replaceElements(int[] arr) {
        /*
        倒序法replace只需要for循环一次
        */
        int next = arr[arr.length-1];
        int max_right = next;
        arr[arr.length-1] = -1;
        for(int j = arr.length-2; j > -1; j--)
        {            
            if( next > max_right ) max_right = next;
            next = arr[j];
            arr[j] = max_right;
        }        
        return arr;
    }
}
