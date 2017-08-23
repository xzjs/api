package t;

import org.zeromq.ZMQ;

public class Zmq {
    public void start() {
        ZMQ.Context context = ZMQ.context(1);
        ZMQ.Socket socket = context.socket(ZMQ.REP);
        socket.bind("tcp://*:5555");
        while (!Thread.currentThread().isInterrupted()) {
            String request = socket.recvStr();
            System.out.println("receive:" + request);
            XFController xfc = new XFController();
            String name = xfc.make(request);
            socket.send(name);
        }
    }
}
