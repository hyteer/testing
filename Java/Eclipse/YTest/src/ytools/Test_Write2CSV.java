package ytools;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import ytools.Write2CSV;
import java.io.FileReader;
import java.io.BufferedReader; 

public class Test_Write2CSV {

	public static void main(String[] args) {          
        String[] colNames = {"第一列","第二列","第三列","第四列"};  
        File csvFile = Write2CSV.createFileAndColName("F:/temp", "write2csv_test2.csv", colNames); 
        
        File inFile = new File("F://Temp//in.csv"); // 读取的CSV文件


        List<String> list = new ArrayList<>();  
        list.add("test data");  
        list.add("test data");  
        list.add("test data3");  
        list.add("test data");  
        List<String> list2 = new ArrayList<>();  
        list2.add("112");  
        list2.add("22");  
        list2.add("32");  
        list2.add("42");  
        List<List<String>> data = new ArrayList<>();  
        data.add(list);  
        data.add(list2);  
        Write2CSV.appendData(csvFile, data);  
        Write2CSV.appendData(csvFile, data); 
        Write2CSV.appendData(inFile, data); 
        
        System.out.println(list.toString());
        System.out.println(data);   
        System.out.println( "Encoding: " + System.getProperty("file.encoding") );  
    }
	
}
