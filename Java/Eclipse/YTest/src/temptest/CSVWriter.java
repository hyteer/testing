package temptest;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

import ytools.Write2CSV;

public class CSVWriter {
    public static void main(String[] args){
        String [] str = {"省","市","区","街","路","里","幢","村","室","园","苑","巷","号"};
        //String[] colNames = {"第一列","第二列","第三列","第四列"};
        File csvFile = Write2CSV.createFileAndColName("F:/temp", "in.csv", str);
        File inFile = new File("F://Temp//in.csv"); // 读取的CSV文件
        File outFile = new File("F://Temp//out.csv");//写出的CSV文件
        String inString = "";
        String tmpString = "";
        try {
            BufferedReader reader = new BufferedReader(new FileReader(inFile));
            BufferedWriter writer = new BufferedWriter(new FileWriter(outFile));
            while((inString = reader.readLine())!= null){
                for(int i = 0;i<str.length;i++){
                    tmpString = inString.replace(str[i], "," + str[i] + ",");
                    inString = tmpString;
                }
               writer.write(inString);
               writer.newLine();
            }
            reader.close();
            writer.close();
        } catch (FileNotFoundException ex) {
            System.out.println("没找到文件！");
        } catch (IOException ex) {
            System.out.println("读写文件出错！");
        }
    }} 

