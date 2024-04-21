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
            DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
            while (true)
            {
                BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                String response = inFromServer.readLine();
                
                if (response.equals("close"))
                {
                    break;
                }
                System.out.println("From server: " + response);
                System.out.println("Input data for server: ");
                String serverInput = inFromUser.readLine();
                outToServer.writeBytes(serverInput);
                
            }
            clientSocket.close();
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}
