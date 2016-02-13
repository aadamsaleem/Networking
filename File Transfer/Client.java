import java.net.*;
import java.io.*;
import java.awt.*;
import java.io.*;
import java.awt.event.*;
import javax.swing.*;

public class Client extends JFrame implements ActionListener{
	
	
	JFrame f;
	public static JTextField jt;
	JButton b;
	
	Client(String s)
	{
		f = new JFrame(s);
		jt = new JTextField("Insert Output Filename");
		jt.setBounds(40,40,100,100);
		
		b = new JButton("OK");
		b.setBounds(40,40,100,100);
		b.addActionListener(this);
		
		
		f.add(jt);
		f.add(b);
		f.setLayout(new FlowLayout(FlowLayout.CENTER,30,30));
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		f.setSize(300,300);
		f.setVisible(true);
	}
	
	public void actionPerformed(ActionEvent e)
	{
		try
		{
			int filesize=1022;
        int bytesRead;
        int currentTot = 0;
        Socket socket = new Socket("127.0.0.1",15123);
        byte [] bytearray  = new byte [filesize];
        InputStream is = socket.getInputStream();
        FileOutputStream fos = new FileOutputStream(""+jt.getText());
        BufferedOutputStream bos = new BufferedOutputStream(fos);
        bytesRead = is.read(bytearray,0,bytearray.length);
        currentTot = bytesRead;
 
        do {
				bytesRead =
				is.read(bytearray, currentTot, (bytearray.length-currentTot));
				if(bytesRead >= 0) 
					currentTot += bytesRead;
        } while(bytesRead > -1);
 
        bos.write(bytearray, 0 , currentTot);
        bos.flush();
        bos.close();
        socket.close();
		}
		catch(Exception e1)
		{
			System.out.println(e1+jt.getText());
		}
	}
 
    public static void main (String [] args ) throws IOException {
	
		new Client("Client");
        
      }
}

