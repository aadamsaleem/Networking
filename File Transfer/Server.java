import java.net.*;
import java.io.*;
import java.awt.*;
import java.io.*;
import java.awt.event.*;
import javax.swing.*;

public class Server extends JFrame implements ActionListener{
	
	JFileChooser jfc;
	public static File f;
	
	public Server()
	{
		super(" Server ");  
		jfc =new JFileChooser("\\");
		JButton jb=new JButton("Select File");
		jb.addActionListener(this);
		getContentPane().add(jb);
		setLayout(new FlowLayout());
		setSize(200,200);
		setVisible(true);
	}
	
	public void actionPerformed(ActionEvent e)
	{

		int x=jfc.showOpenDialog(null);
		if(x==JFileChooser.APPROVE_OPTION)
		{
			f=jfc.getSelectedFile();
			String s=jfc.getName(f);
			System.out.println(s);
		}
		if(x==JFileChooser.CANCEL_OPTION)
		{
			System.out.println("cancel");
		}
	}
 
     public static void main (String [] args ) throws IOException {
	 
			new Server();
          
            ServerSocket serverSocket = new ServerSocket(15123);
              Socket socket = serverSocket.accept();
              System.out.println("Accepted connection : " + socket+f);
              File transferFile = new File (""+f);
              byte [] bytearray  = new byte [(int)transferFile.length()];
              FileInputStream fin = new FileInputStream(transferFile);
              BufferedInputStream bin = new BufferedInputStream(fin);
              bin.read(bytearray,0,bytearray.length);
              OutputStream os = socket.getOutputStream();
              System.out.println("Sending Files...");
              os.write(bytearray,0,bytearray.length);
              os.flush();
              socket.close();
              System.out.println("File transfer complete");
            }
}
