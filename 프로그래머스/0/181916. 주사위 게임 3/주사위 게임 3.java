import java.util.Arrays;

class Solution {
    
    public static int solution(int a, int b, int c, int d) {
        int[] dice = {a, b, c, d};
        int[] counts = new int[7]; // 주사위 값의 범위가 1에서 6이므로 크기를 7로 설정

        for (int value : dice) {
            counts[value]++;
        }

        int uniqueCount = 0;
        for (int count : counts) {
            if (count > 0) {
                uniqueCount++;
            }
        }

        switch (uniqueCount) {
            case 1:
                // 모든 주사위가 같은 경우
                for (int i = 1; i < counts.length; i++) {
                    if (counts[i] == 4) {
                        return 1111 * i;
                    }
                }
                break;
            case 2:
                // 두 개의 고유 값이 있는 경우
                int first = 0, second = 0;
                for (int i = 1; i < counts.length; i++) {
                    if (counts[i] > 0) {
                        if (first == 0) {
                            first = i;
                        } else {
                            second = i;
                        }
                    }
                }
                if (counts[first] == 3 || counts[second] == 3) {
                    int three = counts[first] == 3 ? first : second;
                    int one = counts[first] == 1 ? first : second;
                    return (int) Math.pow(10 * three + one, 2);
                } else {
                    return (first + second) * Math.abs(first - second);
                }
            case 3:
                // 세 개의 고유 값이 있는 경우
                int doubleValue = 0;
                int[] singles = new int[2];
                int index = 0;
                for (int i = 1; i < counts.length; i++) {
                    if (counts[i] == 2) {
                        doubleValue = i;
                    } else if (counts[i] == 1) {
                        singles[index++] = i;
                    }
                }
                return singles[0] * singles[1];
            case 4:
                // 네 개의 고유 값이 있는 경우
                int minValue = Integer.MAX_VALUE;
                for (int i = 1; i < counts.length; i++) {
                    if (counts[i] > 0 && i < minValue) {
                        minValue = i;
                    }
                }
                return minValue;
        }
        return 0;
    }
}