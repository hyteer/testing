package ytools_bak20161213;

import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class YtMD5 {
    public static final String MD5="MD5";
    public static final String UTF8="UTF-8";

    /**
     *  采用加密算法加密字符串数�? 转成长度�?32的字符串
     * @param str
     * @param algorithm 采用的加密算�?
     * @param charset 指定转化之后的字符串编码
     * @return
     */
    public static String EncryptionStr32(String str, String algorithm,String charset) {
        // 加密之后�?得字节数�?
        byte[] bytes = EncryptionStrBytes(str,algorithm,charset);
        return BytesConvertToHexString(bytes);
    }

    /**
     * 采用加密算法加密字符串数�?  转成长度�?32的字符串
     * @param str   �?要加密的数据
     * @param algorithm 采用的加密算�?
     * @return 字节数据
     */
    public static String EncryptionStr32(String str, String algorithm) {
        return EncryptionStr32(str,algorithm,"");
    }


    /**
     *  采用加密算法加密字符串数�?  转成长度�?16的字符串
     * @param str
     * @param algorithm 采用的加密算�?
     * @param charset 指定转化之后的字符串编码
     * @return
     */
    public static String EncryptionStr16(String str, String algorithm,String charset) {
        return EncryptionStr32(str,algorithm,charset).substring(8,24);
    }

    /**
     * 采用加密算法加密字符串数�? 转成长度�?16的字符串
     * @param str   �?要加密的数据
     * @param algorithm 采用的加密算�?
     * @return 字节数据
     */
    public static String EncryptionStr16(String str, String algorithm) {
        return EncryptionStr32(str,algorithm,"").substring(8,24);
    }

    /**
     * 采用加密算法加密字符串数�?
     * @param str   �?要加密的数据
     * @param algorithm 采用的加密算�?
     * @param charset 指定转化之后的字符串编码
     * @return 字节数据
     */
    public static byte[] EncryptionStrBytes(String str, String algorithm, String charset) {
        // 加密之后�?得字节数�?
        byte[] bytes = null;
        try {
            // 获取MD5算法实例 得到�?个md5的消息摘�?
            MessageDigest md = MessageDigest.getInstance(algorithm);
            //添加要进行计算摘要的信息
            if(null==charset||"".equals(charset)) {
                md.update(str.getBytes());
            }else{
                md.update(str.getBytes(charset));
            }
            //得到该摘�?
            bytes = md.digest();
        } catch (NoSuchAlgorithmException e) {
            System.out.println("加密算法: "+ algorithm +" 不存�?: ");
        } catch (UnsupportedEncodingException e) {
            System.out.println("数据加密指定的编码格式不支持: " + charset);
        }
        return null==bytes?null:bytes;
    }
    /**
     * 把字节数组转化成字符串返�?
     * @param bytes
     * @return
     */
    public static String BytesConvertToHexString(byte [] bytes) {
        StringBuffer sb = new StringBuffer();
        for (byte aByte : bytes) {
            String s=Integer.toHexString(0xff & aByte);
            if(s.length()==1){
                sb.append("0"+s);
            }else{
                sb.append(s);
            }
        }
        return sb.toString();
    }
}
    