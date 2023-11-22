class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] arrayConcat = new int [nums.length * 2];
        int control = 0;

        for(int i = 0; i < arrayConcat.length; i++){
            if(control > nums.length - 1){
                control = 0;
            }
           arrayConcat[i] = nums[control++];
        }
        return arrayConcat;
        
    }
}