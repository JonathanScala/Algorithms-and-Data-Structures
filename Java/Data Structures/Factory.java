import java.lang.reflect.Array;


public class Factory<T> {
    Class<T> t;

    public Class<T> type() {
        return t;
    }

    public Factory(Class<T> t0) {
        t = t0;
    }

    @SuppressWarnings({"unchecked"})
    protected T[] newArray(int n) {
        return (T[])Array.newInstance(t, n);
    }

    public T newInstance() {
        T x;
        try {
            x = t.newInstance();
        } catch (Exception e) {
            x = null;
        }
        return x;
    }
}
