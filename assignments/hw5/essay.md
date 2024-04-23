<!-- hotfix: KaTeX -->
<!-- https://github.com/yzane/vscode-markdown-pdf/issues/21/ -->
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">MathJax.Hub.Config({ tex2jax: { inlineMath: [['$', '$']] }, messageStyle: 'none' });</script>

# Sorting essay

Sorting and searching algorithms are essential for computer science,
facilitating efficient data retrieval and manipulation. Their primary goal is to
optimize the data analysis process to minimize computational workload and
preserve resources.

## Sorting

At its core, sorting rearranges items of a collection based on the comparisons
of their value. For instance, an ascending sort of alphabetical name prioritizes
elements with an earlier letter, placing "John" after "Doe." The sorting
algorithm can be applied to any data type provided that the comparator can
determine their relative order.

1.  **Selection sort:** It represents the most basic sorting algorithm (or
    arguably bubble sort), involving element swapping of gradually increasing
    indices. While easy to implement, it is not recommended for large datasets
    due to its inefficiency.
1.  **Merge sort:** A methodical sorting derived from the divide-and-conquer
    approach that is stable, meaning indices of equal values are left untouched.
    Merge sort is favorable for a guaranteed $O(n \log n)$ worst time
    complexity (Programiz, n.d.).
1.  **Quicksort:** Another divide-and-conquer method that utilizes a pivot
    point, it often outperforms merge sort but has the potential to be worse if
    the chosen pivot is continuously unfavorable. Quicksort is the default
    implementation of primitive array sorting in Java (Baeldung, 2024).

## Searching

Searching picks an item from a collection with a specific attribute matched by
the search predicate. One common application of search algorithms is finding the
maximum value of numbers, which helps to get the highest price for retail
products. Unlike sorting, search algorithms do not modify an item's position.

1.  **Linear search:** As the name suggests, it sequentially checks each element
    until the target is found or the end of the collection is reached. It is
    straightforward but proven time-consuming.
1.  **Binary search:** Separates the collection into two halves and discards the
    one that doesn't contain the target, halving the workload on each step.
    Binary search is only applicable to sorted collections.

## References

<ul style="list-style-type: none; padding: 0; line-height: 2.0;">
  <li style="text-indent: -4em; margin-left: 4em;">
    Programiz. (n.d.). <i>Sorting algorithms</i>. Retrieved from Programiz:
    https://www.programiz.com/dsa/sorting-algorithm/
  </li>
  <li style="text-indent: -4em; margin-left: 4em;">
    Baeldung. (2024, February 9). <i>Time Comparison of Arrays.sort(Object[])
    and Arrays.sort(int[])</i>. Retrieved from Baeldung:
    https://www.baeldung.com/arrays-sortobject-vs-sortint/
  </li>
</ul>
