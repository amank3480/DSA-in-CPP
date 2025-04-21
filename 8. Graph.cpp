#include <iostream>
using namespace std;
#include<string.h>
struct node
{
    char data;
    node *left;
    node *right;
};

class tree
{
    char prefix[20];

public:
    node *top;
    void expression(char[]);
    void display(node *);
    void non_rec_postorder(node *);
    void del(node *);
};

class stack1
{
    node *data[30];
    int top;

public:
    stack1()
    {
        top = -1;
    }
    int empty()
    {
        return top == -1;
    }
    void push(node *p)
    {
        data[++top] = p;
    }
    node *pop()
    {
        return (top >= 0) ? data[top--] : NULL;
    }
};

void tree::expression(char prefix[])
{
    stack1 s;
    node *t1, *t2;
    int len = strlen(prefix);
    for (int i = len - 1; i >= 0; i--)
    {
        node *newNode = new node;
        newNode->left = NULL;
        newNode->right = NULL;
        newNode->data = prefix[i];
        if (isalpha(prefix[i]))
        {
            s.push(newNode);
        }
        else if (prefix[i] == '+' || prefix[i] == '*' || prefix[i] == '-' || prefix[i] == '/')
        {
            t2 = s.pop();
            t1 = s.pop();
            newNode->left = t2;
            newNode->right = t1;
            s.push(newNode);
        }
    }
    top = s.pop();
}

void tree::display(node *root)
{
    if (root != NULL)
    {
        cout << root->data;
        display(root->left);
        display(root->right);
    }
}

void tree::non_rec_postorder(node *top)
{
    stack1 s1, s2;
    node *T = top;
    cout << "\nPostorder Traversal: ";
    s1.push(T);
    while (!s1.empty())
    {
        T = s1.pop();
        s2.push(T);
        if (T->left != NULL)
            s1.push(T->left);
        if (T->right != NULL)
            s1.push(T->right);
    }
    while (!s2.empty())
    {
        cout << s2.pop()->data << " ";
    }
    cout << endl;
}

void tree::del(node *node)
{
    if (node == NULL)
        return;
    del(node->left);
    del(node->right);
    cout << "Deleting node: " << node->data << endl;
    delete node;
}

int main()
{
    char expr[20];
    tree t;
    cout << "Enter prefix Expression: ";
    cin >> expr;
    t.expression(expr);
    t.non_rec_postorder(t.top);
    t.del(t.top);
    return 0;
}
