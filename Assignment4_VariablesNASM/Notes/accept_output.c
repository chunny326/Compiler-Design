#include <stdio.h>
#define print(X) _Generic((X), int     \
                          : print_int, \
                            double     \
                          : print_float)(X)

int counter = 0;

int print_int(int i) {
  return printf("%d %d\n", counter++, i);
}

int print_float(double f) {
  return printf("%d %f\n", counter++, f);
}

int print_unknown() {
  return printf("ERROR: Unknown type\n");
}

int main() {
  int var1 = 2;
  print(var1);  // 2
  int var2 = var1 + var1;
  print(var2);
  int var3 = var1 * var2;
  print(var3);
  int var4 = var3 - var2;
  print(var4);
  int var5 = var4 / var3;
  print(var5);
  int var6 = var1 + var2 * var3;
  print(var6);
  int var7 = var4 - var1;
  print(var7);
  int var8 = 3 * 4;
  print(var8);
  int var9 = 12 / 6;
  print(var9);
  int var10 = 12 / 6;
  print(var10);
  int var11 = 5 + 4 * 3;
  print(var11);
  int var12 = 12 + 34 * 45;
  print(var12);
  int var13 = (6 / 5);
  print(var13);
  int var14 = 2 * 2 + 5 * 5;
  print(var14);
  int var15 = 42;
  print(var15);
  int var16 = (42);
  print(var16);
  int var17 = ((42));
  print(var17);
  int var18 = ((42));
  print(var18);
  int var19 = var1;
  print(var19);
  int var20 = var1 + var19;
  print(var20);
  int var21 = var1 + var2;
  print(var21);
  int var22 = var9 * var10;
  print(var22);
  int var23 = var1 + var2 * var3;
  print(var23);
  int var24 = var19 - var20;
  print(var24);
  int var25 = 1234 * 5678;
  print(var25);
  int var26 = 100000 / var13;
  print(var26);
  int var27 = ((12 - 8) - 3);
  print(var27);
  int var28 = (5 * (8 / 4));
  print(var28);
  int var29 = (1 + 2) * 3;
  print(var29);
  int var30 = ((var1 / var2) + (var3 * var4));
  print(var30);
  int a = 1;
  int a_ = 2;
  int v_____2 = 2;
  int v__3__ = 3;
  int var31 = a_;
  print(var31);
  int var32 = (a_);
  print(var32);
  int var33 = (v_____2 + v__3__);
  print(var33);
  int var34 = ((((300 + var1))));
  print(var34);
  int var35 = (var33 - var2) + 18;
  print(var35);
  int var36 = (((((9 + (2 * (110 - (30 / 2)))) * 8) + 1000) / 2) + (((3 * 3 * 3 * 3) + 1) / 2));
  print(var36);
  int var37 = 2 + 3;
  print(var37);
  int var38 = (var1 + var2);
  print(var38);
  int var39 = -42;
  print(var39);
  int var40 = (-42);
  print(var40);
  int var41 = (-42);
  print(var41);
  int var42 = -var1;
  print(var42);
  int var43 = -1 * var1 / -1;
  print(var43);
  int var44 = 2 - 3;
  print(var44);
  int var45 = 2 - 3;
  print(var45);
  int var46 = 2 - -3;
  print(var46);
  int var47 = 2 - -3;
  print(var47);
  int var48 = -2 - 3;
  print(var48);
  int var49 = -2 - -3;
  print(var49);
  int var50 = -2 - -3;
  print(var50);
  int var51 = (-2 - -3);
  print(var51);
  int var52 = (-2 - -3);
  print(var52);
  int var53 = -2 - (-3);
  print(var53);
  int var54 = -2 - (-3);
  print(var54);
  int var55 = -2 - (-3);
  print(var55);
  int var56 = -2 - (-3 - (4));
  print(var56);
  int var57 = -2 - (-3 - (4));
  print(var57);
  int var58 = -2 - (-3 - (-4));
  print(var58);
  int var59 = -2 - (-2 - (-2 - 2));
  print(var59);
  int var60 = -2 - (-2 - (-2 - 2));
  print(var60);
  int var61 = -11 - (-22 - (-33 - (-44 - (-55 - (-66)))));
  print(var61);
  int var62 = 2 - -3;
  print(var62);
  int var63 = 2 + -3;
  print(var63);
  int var64 = 184 + -84;
  print(var64);
  int var65 = 2 - -a;
  print(var65);
  int var66 = 2 + -a;
  print(var66);
  int var67 = 2 + -4;
  print(var67);
  int var68 = 2 + -4;
  print(var68);
  int var69 = 2 + -4;
  print(var69);
  int var70 = 4 * 3 / 2 + 1;
  print(var70);
  int four = 4;
  int three = 3;
  int two = 2;
  int one = 1;
  int var71 = four * three / two + one;
  print(var71);
  int var72 = 4 * 3 / 2 + one;
  print(var72);
  int var73 = (((2 + 3) * 4) + (7 + (8 / 2)));
  print(var73);
  int var74 = (((2 + 3) * 4) + (7 + (var1 / 2)));
  print(var74);
  int var75;
  var75 = 1234;
  print(var75);
  int var76 = 314;
  print(var76);
  double num1 = 1.23456;
  print(num1);
  double num2 = .1;
  print(num2);
  double num3 = 3.14159;
  print(num3);
  double num4 = num2 + num3;
  print(num4);
  double num5 = num2 * num3;
  print(num5);
}