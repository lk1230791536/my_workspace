##LINUX打PATCH简单示例
#生成补丁
diff -u test.c test_1.c > 01_test.patch
#打补丁
patch test.c < 01_test.patch
