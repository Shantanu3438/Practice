class Node {
    int data;
    Node leftNode;
    Node rightNode;

    Node(int data) {
        this.data = data;
    }
}

class BinarySearchTree {
    Node root = null;

    void insert(int data) {
        root = insertNode(root, data);
    }

    Node insertNode(Node root, int data) {
        if(root == null){
            return new Node(data);
        }

        if(data < root.data)
            root.leftNode = insertNode(root.leftNode, data);
        else if(data > root.data)
            root.rightNode = insertNode(root.rightNode, data);
        
        return root;
    }

    void inorder(Node root) {
        if(root != null){
            inorder(root.leftNode);
            System.out.println(root.data);
            inorder(root.rightNode);
        }
    }

    boolean search(Node root, int key) {
        if(root == null)
        return false;
        if(key == root.data)
            return true;
        else if(key < root.data)
            return search(root.leftNode, key);
        else
            return search(root.rightNode, key);
    }

    void delete(int data) {
        root = deleteNode(root, data);
    }

    Node deleteNode(Node root, int data) {
        if(root == null)
            return root;
        else if (data < root.data){
            root.leftNode = deleteNode(root.leftNode, data);
        }
        else if (data > root.data){
            root.rightNode = deleteNode(root.rightNode, data);
        }
        else{
        if(root.leftNode == null)
            return root.rightNode;
        else if(root.rightNode == null)
            return root.leftNode;
            root.data = findLargestNodeData(root.leftNode);
            root.leftNode = deleteNode(root.leftNode, root.data);
    }
        return root;
    }

    int findLargestNodeData(Node root) {
        if(root.leftNode == null)
            return root.data;
        else
            findLargestNodeData(root.leftNode);
        return root.data;
    }
}

class Tree {
    public static void main(String args[]) {
        BinarySearchTree bst = new BinarySearchTree();
	    bst.inorder(bst.root);
    }
}
