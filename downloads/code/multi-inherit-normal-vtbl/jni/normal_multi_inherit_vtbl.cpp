//#include <iostream>
#include <android/log.h>
#include <stdio.h>
#include <string>
//using namespace std;

class A
{
public:
    A(int a = 0):m_a(0){printf("A::constructor()");}
    virtual ~A(){ printf("A::destructor()");}
    virtual void foo(){printf("A::foo()");}
    virtual void hoo(){printf("A::hoo()");}
    void goo(){printf("A::goo()");}
public:
    int m_a;
    // std::string m_name;
    
};

class B:public A{
public:
    B(int b = 0):m_b(b){printf("B::constructor()");}
    virtual ~B(){printf("B::destructor()");}
    virtual void foo(){printf("B::foo()");}
    virtual void hoo(){printf("B::hoo()");}
    virtual void ioo(){printf("B::ioo()");}
public:
    int m_b;
};

class C:public A{
public:
    C(int c = 0):m_c(0){printf("C::constructor()");}
    virtual ~C(){printf("C::destructor()");}
    virtual void foo(){printf("C::foo()");}
    virtual void joo(){printf("C::joo()");}
public:
    int m_c;
};

class D:public B,public C{
public:
    D(int d = 0):m_d(d){printf("D::constructor()");}
    virtual ~D(){printf("D::destructor");}
    virtual void foo(){printf("D::foo()");}

public:
    int m_d;
};

int test(int argc,char* argv[]){
    A a;
    B b;
    C c;
    D d;

   a.foo();
   b.foo();
   c.foo();
   d.foo();
   //cout << "size of a:" << sizeof(a) << endl;
   //cout << "size of b:" << sizeof(b) << endl;
   //cout << "size of c:" << sizeof(c) << endl;
   //cout << "size of d:" << sizeof(d) << endl;
   printf("sizeof a:%d",sizeof(a));
   printf("sizeof b:%d",sizeof(b));
   printf("sizeof c:%d",sizeof(c));
   printf("sizeof d:%d",sizeof(d));

   B* pd = new D(1);
   pd->foo();
    return 0;
}
