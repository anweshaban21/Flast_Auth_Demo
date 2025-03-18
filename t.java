import java.util.*;
// import java.lang.*;
// import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
	    Scanner sc=new Scanner(System.in);
	    int t=sc.nextInt();
	    while(t-->0){
	        
	    int n=sc.nextInt();
	    long x=sc.nextInt();
	    long arr[]=new long[n];
	    HashMap<Long,Long> map=new HashMap<>();
	    long max=0;
	    long maxval=0;
	    for(int i=0;i<n;i++){
	        arr[i]=sc.nextLong();
	        map.put(arr[i],map.getOrDefault(arr[i],0L)+1);
	        if(max<=map.get(arr[i])){
	            if(maxval>arr[i] && max==map.get(arr[i])){
	                maxval=arr[i];
	                continue;
	            }
	            max=map.get(arr[i]);
	            maxval=arr[i];
	            //System.out.print(max+" ");
	        }
	    }
	    long p=x*maxval;
	    if(!map.containsKey(p)){
	        System.out.println(max);
	        continue;
	    }
	    long c=0;
	    int start=-1,end=-1;
	    for(int i=0;i<n;i++){
	        if(arr[i]==maxval && start==-1 ){
	            start=i;
	        }
	        else if(arr[i]==maxval){
	            end=i;
	        }
	    }
	    for(int i=0;i<n;i++){
	        if(arr[i]==p && i>start && i<end)
	            c++;
	    }
	    long ans=map.get(p);
	    //System.out.println(ans+max-c);
	    }
	    
	    
		// your code goes here

	}
}
