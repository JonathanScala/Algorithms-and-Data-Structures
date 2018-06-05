import java.util.AbstractList;
import java.util.Collections;
import java.util.List;


public class RootishArrayDeque<T> extends AbstractList<T> {
    List<T> front;
    List<T> back;
    Class<T> f;

    public RootishArrayDeque(Class<T> t) {
        f = t;
        front = new RootishArrayStack<>(t);
        back = new RootishArrayStack<>(t);
    }

    public void rebalance(){
        int n = size();
        if (back.size() > 3 * front.size()){
            int s = n/2 - front.size();
            List<T> l1 = new RootishArrayStack<>(f);
            List<T> l2 = new RootishArrayStack<>(f);
            l1.addAll(back.subList(0,s));
            Collections.reverse(l1);
            l1.addAll(front);
            l2.addAll(back.subList(s, back.size()));
            front = l1;
            back = l2;

        }
        else if (front.size() > 3 * back.size()){
            int s = front.size() - n/2;
            List<T> l1 = new RootishArrayStack<>(f);
            List<T> l2 = new RootishArrayStack<>(f);
            l1.addAll(front.subList(s, front.size()));
            l2.addAll(front.subList(0, s));
            Collections.reverse(l2);
            l2.addAll(back);
            front = l1;
            back = l2;


        }
    }

    public T get(int i) {
        if (i < 0 || i > size() - 1) throw new IndexOutOfBoundsException();

        T item;
        if (i < front.size())
            item = front.get(front.size() - i - 1);
        else
            item = back.get(i - front.size());
        return item;
    }

    public T set(int i, T x) {
        if (i < 0 || i > size() - 1) throw new IndexOutOfBoundsException();

        T item;
        if (i < front.size())
            item = front.set(front.size() - i - 1, x);
        else
            item = back.set(i - front.size(), x);
        return item;
    }

    public void add(int i, T x) {
        if (i < 0 || i > size()) throw new IndexOutOfBoundsException();

        if (i < front.size())
            front.add(front.size() - i, x);
        else
            back.add(i - front.size(), x);
        rebalance();
    }

    public T remove(int i) {
        if (i < 0 || i > size() - 1) throw new IndexOutOfBoundsException();

        T item;
        if (i < front.size())
            item = front.remove(front.size() - i - 1);
        else
            item = back.remove(i - front.size());
        rebalance();
        return item;
    }

    public int size() {
        return front.size() + back.size();
    }

    public static void main(String[] args) {
    }
}
