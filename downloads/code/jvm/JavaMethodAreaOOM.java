/**
 * javac -cp ".:./cglib-nodep-3.2.12.jar" JavaMethodAreaOOM.java
 * java -XX:PermSize=10M -XX:MaxPermSize=10M -cp ".:./cglib-nodep-3.2.12.jar" JavaMethodAreaOOM
 */

import java.lang.reflect.Method;
import net.sf.cglib.proxy.Enhancer;
import net.sf.cglib.proxy.MethodInterceptor;
import net.sf.cglib.proxy.MethodProxy;

 public class JavaMethodAreaOOM{
  public static void main(String[] args){
    while(true){
      Enhancer enhancer = new Enhancer();
      enhancer.setSuperclass(OOMObject.class);
      enhancer.setUseCache(false);
      enhancer.setCallback(new MethodInterceptor(){
        public Object intercept(Object obj,Method method,Object[] args,MethodProxy proxy)throws Throwable{
          return proxy.invokeSuper(obj,args);
        }
      });
      enhancer.create();
    }
  }

  static class OOMObject{
  }
 }
