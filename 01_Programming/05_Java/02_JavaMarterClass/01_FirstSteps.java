public class FirstSteps {
    public static void main(String[] args) {
        // Hello world
        System.out.println("Hello World");

        int firstVariable = 5;
        System.out.println(firstVariable);

        // Primitive types
        // Eight primitive data types: boolean, byte,
        // char, short, int, long, float and double

        int minIntV = Integer.MIN_VALUE;
        int maxIntV = Integer.MAX_VALUE;
        System.out.println("Min integer value = " + minIntV);
        System.out.println("Max integer value = " + maxIntV);
        System.out.println("Busted min value = " + (minIntV - 1));
        System.out.println("Busted max value = " + (maxIntV + 1));
        int intTest = 2_147_483_647;

        byte minByteV = Byte.MIN_VALUE;
        byte maxByteV = Byte.MAX_VALUE;
        System.out.println("Min byte value = " + minByteV);
        System.out.println("Max byte value = " + maxByteV);

        short minShortV = Short.MIN_VALUE;
        short maxShortV = Short.MAX_VALUE;
        System.out.println("Min short value = " + minShortV);
        System.out.println("Max short value = " + maxShortV);

        long longValue = 100L;

        long minLongV = Long.MIN_VALUE;
        long maxLongV = Long.MAX_VALUE;
        System.out.println("Min long value = " + minLongV);
        System.out.println("Max long value = " + maxLongV);

        // Casting
        //byte newByte = minByteV/2;
        byte newByte = (byte)(minByteV/2);
        short newShort = (short)(minShortV/2);

        // floating point types
        // there are single and double precision types
        float minFloatV = Float.MIN_VALUE;
        float maxFloatV = Float.MAX_VALUE;
        System.out.println("Min float value = " + minFloatV);
        System.out.println("Max float value = " + maxFloatV);

        double minDoubleV = Double.MIN_VALUE;
        double maxDoubleV = Double.MAX_VALUE;
        System.out.println("Min double value = " + minDoubleV);
        System.out.println("Max double value = " + maxDoubleV);

        float myFloat = 5.25f;
        double myDouble = 6.32514d;

        char myChar = 'D';
        char myUnicodeChar = '\u0044';
        System.out.println(myChar);
        System.out.println(myUnicodeChar);

        boolean myBoolean = true;
        myBoolean = false;
        System.out.println(myBoolean);

        // Strings, (String is a class, not a primitive type)
        // String is limited by memory or the max value of an int (2.14billion)
        // Remember that Strings are INMUTABLE, so when you do something like
        // string1 = string1 + "hello", it isn't appending "hello" to string1,
        // it actually create another string and appending "hello" to it
        // it is inefficient.
        String myString = "This is a string";
        System.out.println("My string is equal to " + myString);

        // Operators (+, -, /, *, % , ++, --, +=, -=, *=, /=)

        // if then
        if (myBoolean == false){
            System.out.println("My boolean is false");
        }

        // Logical operators : <, >, !, ==, <=, >=, !=, &&, ||

        // Ternary operator
        // if myBoolean is true, then otherBoolean is true, else is false
        boolean otherBoolean = myBoolean ? true : false;
    }
}
