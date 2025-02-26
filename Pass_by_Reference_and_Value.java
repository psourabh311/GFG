class Solution {
    int b;
    static int[] passedBy(int a, int b) {
        a+=1;
        Solution test = new Solution();
        test.b = b;
        func(test);
        return new int[] {a,test.b};

    }
    static void func(Solution test){
        test.b +=2;
    }
}
