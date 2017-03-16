package ytools;

import java.security.MessageDigest;  
//import java.security.NoSuchAlgorithmException;  

public class MD5Util2 {  
  
	public String md5(String txt) {
        try{
             MessageDigest md = MessageDigest.getInstance("MD5");
             md.update(txt.getBytes("UTF-8"));    //
             StringBuffer buf=new StringBuffer();            
             for(byte b:md.digest()){
                  buf.append(String.format("%02x", b&0xff));        
             }
            return  buf.toString();
          }catch( Exception e ){
              e.printStackTrace(); 

              return null;
           } 
   }
  
}  