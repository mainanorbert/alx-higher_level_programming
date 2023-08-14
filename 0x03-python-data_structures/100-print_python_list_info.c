#include <Python.h>
/**
 * print_python_list_info - prints info on python lists
 * @p: PyObject list
 */

void print_python_list_info(PyObject *p)
{
	PyObject *ob;
	int size, size_all, i;

	size = Py_SIZE(p);
	size_all = (p(PyListObject *))->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", size_all);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		ob = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
