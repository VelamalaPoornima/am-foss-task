defmodule PrimeFinder do
  def is_prime(n) when n <= 1, do: false
  def is_prime(2), do: true
  def is_prime(n) do
    is_prime(n, 2)
  end

  defp is_prime(n, divisor) when divisor * divisor > n, do: true
  defp is_prime(n, divisor) when rem(n, divisor) == 0, do: false
  defp is_prime(n, divisor) do
    is_prime(n, divisor + 1)
  end

  def find_primes(n) when n < 2, do: []
  def find_primes(n) do
    find_primes(n, n, [])
  end

  defp find_primes(1, _, acc), do: Enum.reverse(acc)
  defp find_primes(n, current, acc) when is_prime(current) do
    find_primes(n - 1, current - 1, [current | acc])
  end
  defp find_primes(n, current, acc) do
    find_primes(n - 1, current - 1, acc)
  end
end

IO.puts("Enter a number n:")
n = String.to_integer(IO.gets(""))

if n < 2 do
  IO.puts("There are no prime numbers up to #{n}.")
else
  prime_numbers = PrimeFinder.find_primes(n)
  IO.puts("Prime numbers up to #{n}:")
  Enum.each(prime_numbers, &IO.puts/1)
end
