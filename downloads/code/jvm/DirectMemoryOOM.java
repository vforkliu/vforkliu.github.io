/**
 * java -Xmx20m -XX:MaxDirectMemorySize=10M DirectMemoryOOM
 */

import sun.misc.Unsafe;
import java.lang.reflect.Field;

public class DirectMemoryOOM{
  public static void main(String[] args) throws Exception{
    Field unsafeField = Unsafe.class.getDeclaredFields()[0];
    unsafeField.setAccessible(true);
    Unsafe unsafe = (Unsafe)unsafeField.get(null);
    while(true){
      unsafe.allocateMemory(1024*1024);
    }
  }
}
