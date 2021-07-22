// https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if(nums1.length > nums2.length) {
            int[] temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        } // let nums1 be the smaller array

        int start1 = -1;
        int end1 = nums1.length - 1;
        if(end1 == -1) { // If the first array is empty
            if((nums1.length+nums2.length)%2==0){
                // If it is the true cut for a even total array
                return ((double) (nums2[nums2.length/2-1])+nums2[nums2.length/2]) / 2;
            } else {
                return nums2[nums2.length/2];
            }
        }
        int index1 = nums1.length / 2;
        int medIndex = (nums1.length + nums2.length) / 2 - 1;
        int index2 = medIndex - index1 - 1;
        // if total length is odd, median being the next element after the cut-point
        // when both arrays are not empty, set initial cut-point in the middle of array1 and array2
        // cut the arrays after the cut-point index
        // nums1: ...[index1]|[index1+1]..., nums2: ...[index2]|[index2+1]...
        // complete_array: ...[medIndex]|[medIndex+1]...
        // hence each array have cut-point-index [-1] -> [length-1]

        while(true) {
            if(index1<nums1.length-1  && index1>=0) {
                // If there are four numbers around cut-points
                if(nums1[index1] <= nums2[index2+1] && nums1[index1+1] >= nums2[index2]) {
                    // If it is the true cut-point
                    // System.out.println("If it is the true cut-point");
                    // System.out.println("index1: " + index1 + " index2: " + index2 + " medIndex: " + medIndex);
                    if((nums1.length+nums2.length)%2==0){
                        // If it is the true cut for a even total array
                        return ((double) (Math.max(nums1[index1], nums2[index2]) + Math.min(nums1[index1 + 1], nums2[index2 + 1]))) / 2;
                    } else {
                        return Math.min(nums1[index1+1], nums2[index2+1]);
                    }
                }
                if(nums1[index1] > nums2[index2+1]) { // ind1 too large, go left
                        end1 = index1 - 1;
                } else { // ind1 too small,  go right
                        start1 = index1 + 1;
                }
                index1 = (start1 + end1) / 2;
                index2 = medIndex - index1 - 1;
            } else if(index1==nums1.length-1 && index2<nums2.length-1 && index2>=0) {
                // index1 at the right-most, index2 in the middle
                // it has to be the true cut // OR NOT
                if(nums1[index1] <= nums2[index2+1]) { // If it is the true cut
                    // System.out.println("index1 at the right-most, index2 in the middle");
                    // System.out.println("index1: " + index1 + " index2: " + index2 + " medIndex: " + medIndex);
                    if ((nums1.length + nums2.length) % 2 == 0) {
                        // If it is the true cut for a even total array
                        return ((double) (Math.max(nums1[index1], nums2[index2]) + nums2[index2 + 1])) / 2;
                    } else {
                        return nums2[index2 + 1];
                    }
                } else { // it is not the true cut, move index1 left
                    end1 = index1 - 1;
                    index1 = (start1 + end1) / 2;
                    index2 = medIndex - index1 - 1;
                }
            } else if(index1==-1 && index2<nums2.length-1 && index2>=0) {
                // index1 at the left-most, index2 in the middle
                // it has to be the true cut // OR NOT
                if(nums1[0] >= nums2[index2]){
                    // System.out.println("index1 at the left-most, index2 in the middle");
                    // System.out.println("index1: " + index1 + " index2: " + index2 + " medIndex: " + medIndex);
                    if ((nums1.length + nums2.length) % 2 == 0) {
                        // If it is the true cut for a even total array
                        return ((double) (nums2[index2] + Math.min(nums1[index1 + 1], nums2[index2 + 1]))) / 2;
                    } else {
                        return Math.min(nums1[index1 + 1], nums2[index2 + 1]);
                    }
                } else { // it is not the true cut, move index1 right
                    start1 = index1 + 1;
                    index1 = (start1 + end1) / 2;
                    index2 = medIndex - index1 - 1;
                }

            } else if(index1==nums1.length-1 && index2 == -1) {
                // index1 at the right-most, index2 at the left-most
                if(nums1[index1] <= nums2[0]){
                    // System.out.println("index1 at the right-most, index2 at the left-most");
                    // System.out.println("index1: " + index1 + " index2: " + index2 + " medIndex: " + medIndex);
                    if ((nums1.length + nums2.length) % 2 == 0) {
                        // If it is the true cut for a even total array
                        return ((double) (nums1[nums1.length - 1]) + nums2[0]) / 2;
                    } else {
                        return nums2[0];
                    }
                } else { // it is not the true cut, move index1 left
                    end1 = index1 - 1;
                    index1 = (start1 + end1) / 2;
                    index2 = medIndex - index1 - 1;
                }
            } else if(index1==-1 && index2 == nums2.length-1) {
                // index1 at the left-most, index2 at the right-most
                if(nums2[index2] <= nums1[0]){
                    // System.out.println(" index1 at the left-most, index2 at the right-most");
                    // System.out.println("index1: " + index1 + " index2: " + index2 + " medIndex: " + medIndex);
                    if ((nums1.length + nums2.length) % 2 == 0) {
                        // If it is the true cut for a even total array
                        return ((double) (nums2[nums2.length - 1]) + nums1[0]) / 2;
                    } else {
                        return nums1[0];
                    }
                } else { // it is not the true cut, move index1 right
                    start1 = index1 + 1;
                    index1 = (start1 + end1) / 2;
                    index2 = medIndex - index1 - 1;
                }
            }
            // since nums1 is shorter than nums2, there won't be a time when index2 is at edge while index1 still in middle
        }
    }
}