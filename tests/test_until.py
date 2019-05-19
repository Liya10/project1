{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from Adversary.utils import *\n",
    "\n",
    "def test_flatten_unique():\n",
    "    l = [[1, 2], [1, 3, 4], [5]]\n",
    "    assert(flatten_unique(l) == [1, 2, 3, 4, 5])\n",
    "\n",
    "def test_combinations_of_len():\n",
    "    l = [1, 2, 3]\n",
    "    assert(combinations_of_len(l, 2) == [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3)])\n",
    "\n",
    "def test_fancy_titles():\n",
    "    cols = ['change_case', 'insert_duplicate_characters', 'synonym']\n",
    "    assert(fancy_titles(cols) == ['Change Case', 'Insert Duplicate Characters', 'Synonym'])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
