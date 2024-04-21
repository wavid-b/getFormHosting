import java.io.*;
import java.net.*;

public class client 
{
    public static void main(String[] args) throws Exception 
    {
        System.out.println("Input host IP address: ");
        BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
        String ipAddress = inFromUser.readLine();
        try 
        {
            Socket clientSocket = new Socket(ipAddress, 8099);
            OutputStreamWriter outToServer = new OutputStreamWriter(clientSocket.getOutputStream(), "UTF-8");       
            BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream(), "UTF-8"));     
        while (true)
            {
                String response = null;
                while (!inFromServer.ready()){
                    Thread.sleep(100);  
                }
                response = inFromServer.readLine();
                if (response.equals("close") || response.equals("close \n"))
                {
                    break;
                }
                System.out.println("From server: " + response);
                System.out.println("Input data for server: ");
                String serverInput = inFromUser.readLine();
                outToServer.write(serverInput);
                outToServer.flush();
            }
            clientSocket.close();
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}
