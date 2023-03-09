#the input should be given with spaces between sign bit,exponent bits and mantissa bits
print("\t\tFLOATING POINT TO DECIMAL CONVERTER\n")
while(True):
        print("Enter floating point with only 0,1 and spaces :")
        fp=input()
        if(str(0) in fp and str(1) and fp and " " in fp):
            s=fp.split(' ')
            sign=int(s[0])
            spexponent=int(s[1],2)-127
            dpexponent=int(s[1],2)-1023
            sum=0
            for i in range(len(s[2])):
                    if(int(s[2][i])==1):
                            sum+=(2**(-i-1))
            montissa=sum
            dec1=((-1)**sign)*(1+montissa)*(2**(spexponent))
            dec2=((-1)**sign)*(1+montissa)*(2**(dpexponent))
            if(sign==0):
                print("DECIMAL REPRESENTATION (SINGLE PRECISION): ",1+montissa,"x 2 ^",spexponent)
                print("DECIMAL REPRESENTATION (DOUBLE PRECISION): ",1+montissa,"x 2 ^",dpexponent)
            else:
                print("DECIMAL REPRESENTATION : ","-",1+montissa,"x 2 ^",spexponent)
                print("DECIMAL REPRESENTATION : ","-",1+montissa,"x 2 ^",dpexponent)
            print("DECIMAL VALUE (SINGLE PRECISION): ",dec1)
            print("DECIMAL VALUE (DOUBLE PRECISION): ",dec2)
            print("\n")
        else:
            print("PLEASE, ONLY ENTER 0'S AND 1'S")
            print()
        True
