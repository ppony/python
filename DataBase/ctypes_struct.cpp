
#include <stdio.h>
#include <string.h>

typedef struct _SimpleStruct  
{  
    int    nNo;  
    float  fVirus;  
    char   szBuffer[512];  
} SimpleStruct, *PSimpleStruct;  

typedef const SimpleStruct*  PCSimpleStruct;  
  
extern "C" int  __declspec(dllexport) PrintStruct(PSimpleStruct simp);  
int PrintStruct(PSimpleStruct simp)  
{  
    strcpy (simp->szBuffer, "wowwooo");
    printf ("nMaxNum=%f, szContent=%s", simp->fVirus, simp->szBuffer);  
    printf ("nMaxNum=%f, nono=%d", simp->fVirus, simp->nNo);  
    simp->nNo=5;
    return simp->nNo;  
}  


__declspec(dllexport) int sum(int a, int b) {
    return a + b;
}
