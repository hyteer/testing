package ytools;

import java.io.BufferedWriter;  
import java.io.File;  
import java.io.FileNotFoundException;  
import java.io.FileOutputStream;  
import java.io.FileWriter; 
import java.io.FileReader;
import java.io.IOException;  
import java.io.OutputStream;  
import java.io.OutputStreamWriter;  
import java.io.PrintWriter;  
import java.io.RandomAccessFile;  
import java.util.ArrayList;  
import java.util.List;  
import java.util.Map;  
  
  
public class Write2CSV {  
      
    public static File createFileAndColName(String filePath, String fileName,  String[] colNames){  
        File csvFile = new File(filePath, fileName);  
        PrintWriter pw = null;  
        try {             
            pw = new PrintWriter(csvFile, "GBK");         
            StringBuffer sb = new StringBuffer();  
            for(int i=0; i<colNames.length; i++){  
                if( i<colNames.length-1 )  
                    sb.append(colNames[i]+",");  
                else  
                    sb.append(colNames[i]+"\r\n");  
                  
            }  
            pw.print(sb.toString());  
            pw.flush();  
            pw.close();  
            return csvFile;           
        } catch (Exception e) {  
            e.printStackTrace();  
        }                 
        return null;  
    }  
      
    public static boolean appendData(File csvFile, List<List<String>> data){         
        try {  
              
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(csvFile, true), "GBK"), 1024);  
            for(int i=0; i<data.size(); i++){  
                List tempData = data.get(i);  
                StringBuffer sb = new StringBuffer();  
                for(int j=0; j<tempData.size(); j++){                      
                    if(j<tempData.size()-1)  
                        sb.append(tempData.get(j)+",");  
                    else  
                        sb.append(tempData.get(j)+"\r\n");                    
                }                 
                bw.write(sb.toString());  
                if(i%1000==0)  
                    bw.flush();  
            }             
            bw.flush();  
            bw.close();  
              
            return true;              
        } catch (Exception e) {  
            e.printStackTrace();  
        }                 
        return false;  
    }  
      
      
 
      
      
      
}

