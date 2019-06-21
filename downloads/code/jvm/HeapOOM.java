/**
 * java -Xms20m -Xmx20m -XX:+HeapDumpOnOutOfMemoryError HeapOOM
 */

import java.util.List;
import java.util.ArrayList;

 class HeapOOM{
 
  static class OOMObject{
  }

  public static void main(String[] args){
    List<OOMObject> list = new ArrayList<OOMObject>();
    while(true){
      list.add(new OOMObject());
    }
  }

 }
