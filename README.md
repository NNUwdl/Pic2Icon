# Pic2Icon

Coding while Learning

English Version

This is a file using to convert icon from *.jpg,*.png,*.jpeg image files.

To use this program to convert to icon from *.jpg,*.png,*.jpeg files, You just need to double click Pic2Icon.exe. Wait until it shows the guidance. Drag the image file you want to process into the command box. Wait for it to finish processing. That's all.
It will try to open the output_icon after conversion.

The output icon will be put in the Output_Icon folder of the input file directory.

This software is mainly made by using model pillow, opencv and numpy.(this environment is not required on your computer)

There are still some problems to be solved. For example, using Python window modules will make the user interface more user-friendly. For example, Image re-sampling into 2048 x2048 cv2.resize function is used. The resize function expand the array. I found that the method can raise the sharpness of the picture, because it will not change an array by the values, such as resampling points located in the junction of two colors in the artwork, that it should take another color similar to both color, but the resize function has failed to do so.

Thank you for using my software.

@Auther : NNUwdl @Email : nnuwxl@gmail.com

中文版(Chinese version)

此程序实现将*.jpg、 *.jpeg、*.png格式的图片转化成\*ico格式 系统支持的icon图标，您可以将输出的图标用于改变文件夹和快捷方式的显示。

使用流程： 您只需要双击Pic2Icon.exe， 稍等片刻，它便会在屏幕上显示提示信息， 将要处理的图片文件拖到命令框中，或是填入(相对\绝对)路径， 等待它解析路径，并全部处理完成即可。在程序处理完成后会尝试打开输出的icon文件。

输出的icon图标在输入文件目录的Output_Icon文件夹下。

此软件输出的icon图标的分辨率是2048x2048的，因此输出文件的清晰度会比网站转换的清晰度会高上许多。
因为输出的icon图标是四通道的RGBA图片，所以支持将四通道PNG图片输入，并且输出的时候会原样保留PNG的A通道
对于不是正方形图片，该程序的解决方法是补全成正方形，补充的像素四通道设置为\[0 0 0 0](透明)

此程序主要基于python的pillow、opencv和numpy库（在您电脑上不需要拥有这个环境）

还有一些问题等待解决。 比如可以使用python的窗口模块让用户界面更友好。比如将图片重采样成2048x2048时运用的是cv2.resize函数将数组扩充，个人发现这样的方法会增加图片的锐度，因为它好像并不会改变数组的值，比如说重采样的点在原图中位于两个颜色的交界处，那它其实应该取中间色，但是resize函数并没有这样做。

感想您使用本软件。

@作者 : NNUwdl @邮箱 : nnuwxl@gmail.com
