import java.util.*;
class CP285 {
public static void main(String args[]) {
	int[] buildingHeight = new int[]{3, 7, 8, 3, 6, 1};
	int size = 6;
	int count = 1;
	int largestBuilding =  buildingHeight[size - 1];
	int[] buildView = new int[6];
	buildView[0] = buildingHeight[size - 1];
	for(int i = size - 1; i > 0; i--) {
		if(largestBuilding < buildingHeight[i - 1]){
		largestBuilding = buildingHeight[i - 1];
		buildView[count++] = largestBuilding;
		}
	}
	
	for(int i = 0; i < size - 1; i++) {
	System.out.println(buildView[i]);
	}	
}
}
