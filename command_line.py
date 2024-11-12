import sys
'''This function iterates through the sys.argv function and checks it to see if the value is a float or not. It then tries and sees if the float can be added; 
if not it will keep tryign to see if it can add each item can be added to result. at the end of the iterations, it returns the total sum of the list'''
def main()->float:
    result = 0
    for item in sys.argv:
        try:
            result = result + float(item)
        except ValueError:
            continue
    print(result)
    return result

if __name__ == '__main__':
    main()
    print(sys.argv)