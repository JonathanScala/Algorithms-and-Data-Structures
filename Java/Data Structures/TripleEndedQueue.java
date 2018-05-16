import java.util.AbstractList;
import java.util.LinkedList;
import java.util.List;


public class TripleEndedQueue<T> extends AbstractList<T> {
    LinkedList<T> front;
    LinkedList<T> back;

    public TripleEndedQueue(Class<T> type) {
        front = new LinkedList<>();
        back = new LinkedList<>();
    }

    public void rebalance(){
        if (front.size() - back.size() == 2){
            T item = front.removeLast();
            back.addFirst(item);
        }
        else if (back.size() - front.size() == 2){
            T item = back.removeFirst();
            front.addLast(item);
        }
    }

    public T get(int i) {
        if (i < 0 || i > size() - 1) throw new IndexOutOfBoundsException();
        if (i < front.size())
            return front.get(i);
        else
            return back.get(i - front.size());
    }

    public T set(int i, T x) {
        if (i < 0 || i > size() - 1) throw new IndexOutOfBoundsException();
        if (i < front.size())
            return front.set(i, x);
        else
            return back.set(i - front.size(), x);
    }

    public void add(int i, T x) {
        if (i < 0 || i > size()) throw new IndexOutOfBoundsException();
        if (i < front.size())
            front.add(i, x);
        else
            back.add(i-front.size(), x);
        rebalance();
    }

    public T remove(int i) {
        if (i < 0 || i > size() - 1) throw new IndexOutOfBoundsException();
        T item;
        if (i < front.size())
            item = front.remove(i);
        else
            item = back.remove(i-front.size());
        rebalance();
        return item;
    }

    public int size() {
        return front.size() + back.size();
    }

    public static void main(String[] args) {
    }
}
