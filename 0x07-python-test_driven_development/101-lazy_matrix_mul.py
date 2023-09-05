#!/usr/bin/python3
"""importing the numpy module"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiplying two natrices and returns a matrix

    Args:
        m_a (matrix): matrix of lists
        n_b (matrix): matrix made of lists
    """
    return (numpy.matmul(m_a, m_b))
