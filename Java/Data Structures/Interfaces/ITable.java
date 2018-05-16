public interface ITable<T> {
    public int rows();
    public int cols();
    public T get(int i, int j);
    public T set(int i, int j, T x);
    public void addRow(int i);
    public void removeRow(int i);
    public void addCol(int j);
    public void removeCol(int j);
    public String toString();
}
