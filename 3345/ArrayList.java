public class MyArrayList<AnyType> implements Iterable<AnyType> {
    private static final int DEFAULT_CAPACITY = 10;

    private int size;
    private AnyType[] arr;
    // use .length for capacity

    // Capacity
    private void changeCapacity(int newCapacity) {
        if (newCapacity < size) {
            return;
        }

        AnyType[] newArr = (AnyType[]) new Object[newCapacity];
        for (int i = 0; i < size; i++) {
            newArr[i] = arr[i];
        }

        arr = newArr;
    }

    private int incCapacity(int mult = 2) {
        newCapacity = arr.length * mult + 1;
        changeCapacity(newCapacity);
        return newCapacity;
    }

    // List interface
    public AnyType get(int idx) {
        if (idx < 0 || idx > size) {
            throw new ArrayIndexOutOfBoundsException();
        }

        return arr[idx];
    }

    public AnyType set(int idx, AnyType newVal) {
        if (idx < 0 || idx > size) {
            throw new ArrayIndexOutOfBoundsException();
        }

        AnyType old = arr[idx];
        arr[idx] = newVal;

        return old;
    }

    public void add(int idx, AnyType x) {
        if (idx < 0 || idx > size) {
            throw new ArrayIndexOutOfBoundsException();
        }

        if (size + 1 > arr.length) {
            incCapacity();
        }

        for (int i = size - 1; i >= idx; i--) {
            arr[i + 1] = arr[i];
        }

        arr[idx] = x;
        size++;
    }

    public void remove(int idx) {
        if (idx < 0 || idx > size) {
            throw new ArrayIndexOutOfBoundsException();
        }

        for (int i = idx; i < size - 1; i++) {
            arr[i] = arr[i + 1];
        }

        arr[size - 1] = null;
        size--;
    }

    // Collection interface
    public int size() {
        return size;
    }
    
    public boolean isEmpty() {
        return (size == 0);
    }

    public void clear() {
        size = 0;
        changeCapacity(DEFAULT_CAPACITY);
    }

    public boolean contains(AnyType x) {
        for (AnyType item : arr) {
            if (item == x) {
                return true;
            }
        }
        return false;
    }

    public boolean add(AnyType x) {
        add(size + 1, x);
        return true;
    }

    public boolean remove(AnyType x) {
        for (int i = 0; i < size; i++) {
            if (arr[i] == x) {
                remove(i);
                return true;
            }
        }
        return false;
    }
    public java.util.Iterator<AnyType> iterator() {
        return new ArrayListIterator();
    }
}