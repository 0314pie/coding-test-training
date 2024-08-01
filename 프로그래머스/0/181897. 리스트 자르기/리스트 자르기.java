import java.util.Arrays;

class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        int a = slicer[0];
        int b = slicer[1];
        int c = slicer[2]; 

        switch(n) {
            case 1:
                return Arrays.copyOfRange(num_list, 0, b + 1);
            case 2:
                return Arrays.copyOfRange(num_list, a, num_list.length);
            case 3:
                return Arrays.copyOfRange(num_list, a, b + 1);
            case 4:
                return sliceWithStep(num_list, a, b, c);
            default:
                return new int[0];
        }
    }

    private int[] sliceWithStep(int[] num_list, int start, int end, int step) {
        int length = (end - start) / step + 1;
        int[] result = new int[length];
        int index = 0;
        for (int i = start; i <= end; i += step) {
            result[index++] = num_list[i];
        }
        return result;
    }
}