import java.util.ArrayList;
import java.util.List;

class Reverse {
public static void main(String args[]) {
List<Integer> number = new ArrayList<Integer>();
List<String> result;
number.add(153);
number.add(371);
number.add(1634);
number.add(4374);
Reverse reverse = new Reverse();
result = reverse.armstrong(number);
for(int i = 0; i < result.size(); i++)
    System.out.println(result.get(i));

}

public int revNum(int number) {
int temp = number, result = 0, digits = 0, digit;
while(temp != 0){
    temp /= 10;
    digits++;
}

temp = number;
while(temp != 0) {
    digit = temp % 10;
    result += Math.pow(digit , digits);
    temp /= 10;
}
return result;
}

public List<String> armstrong(List<Integer> arr){
    List<String> result = new ArrayList<String>();
    for(int i = 0; i < arr.size(); i++){
        if(revNum(arr.get(i)) == arr.get(i))
            result.add("It is an armstrong number");
        else
            result.add("It is not an armstrong number");
    }
    return result;
}
}
