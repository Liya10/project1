{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from Adversary.adversary import Adversary\n",
    "\n",
    "def test_generate_single_iter():\n",
    "    m = Adversary(verbose=True)\n",
    "    og_texts = [u'happy happy happy happy dog dog dog dog dog',\n",
    "          u'okay okay yeah here', 'tell me awful things']\n",
    "    g = m.generate(og_texts)\n",
    "    assert(len(g) == 3)\n",
    "\n",
    "def test_generate_many_iter():\n",
    "    m = Adversary(verbose=True)\n",
    "    og_texts = [u'happy happy happy happy dog dog dog dog dog',\n",
    "          u'okay okay yeah here', 'tell me awful things']\n",
    "    g = m.generate(og_texts, text_sample_rate=5)\n",
    "    assert(len(g) == 15)\n",
    "\n",
    "def test_large():\n",
    "    m = Adversary(verbose=True)\n",
    "    og_texts = ['tell me awful things'] * 1000\n",
    "    g = m.generate(og_texts, text_sample_rate=5)\n",
    "    assert (len(g) == 5000)\n",
    "\n",
    "def test_attack():\n",
    "    m = Adversary(verbose=True)\n",
    "    og_texts = [u'happy happy happy happy dog dog dog dog dog',\n",
    "          u'okay okay yeah here', 'tell me awful things']\n",
    "    g = m.generate(og_texts)\n",
    "    df_s, df_m = m.attack(og_texts, g, lambda x: 1 if x in og_texts else 0)\n",
    "    assert(df_s is not None and df_m is not None)\n",
    "\n",
    "def test_attack_large():\n",
    "    m = Adversary(verbose=True)\n",
    "    og_texts = ['tell me awful things'] * 1000\n",
    "    g = m.generate(og_texts)\n",
    "    df_s, df_m = m.attack(og_texts, g, lambda x: 1 if x in og_texts else 0)\n",
    "    assert (df_s is not None and df_m is not None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
