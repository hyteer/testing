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
        String [] str = {"ʡ","��","��","��","·","��","��","��","��","԰","Է","��","��"};
        //String[] colNames = {"��һ��","�ڶ���","������","������"};
        File csvFile = Write2CSV.createFileAndColName("F:/temp", "in.csv", str);
        File inFile = new File("F://Temp//in.csv"); // ��ȡ��CSV�ļ�
        File outFile = new File("F://Temp//out.csv");//д����CSV�ļ�
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
            System.out.println("û�ҵ��ļ���");
        } catch (IOException ex) {
            System.out.println("��д�ļ�����");
        }
    }} 

