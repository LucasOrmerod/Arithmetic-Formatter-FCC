def generate_space(length):
  return " " * length


def arithmetic_arranger(problems, incSum=False):
  print("PROBLEMS:")
  print(problems)
  # Return an error if there are too many problems.
  if len(problems) > 5:
    return "Error: Too many problems."

  # Set the results variable depending on whether or not to find the answer.
  if incSum:
    results = ["", "", "", ""]
  else:
    results = ["", "", ""]

  # Split the problems into three to check criteria.
  for index, problem in enumerate(problems):
    elements = problem.split()

    # Return an error if the operator is not '+' or '-'.
    if elements[1] != "+" and elements[1] != "-":
      return "Error: Operator must be '+' or '-'."

    # Return an error if the numbers do not contain only digits.
    if not elements[0].isdigit() or not elements[2].isdigit():
      return "Error: Numbers must only contain digits."

    # Return an error if any of the numbers contain more than four digits.
    if len(elements[0]) > 4 or len(elements[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    # Perform the calculation to get the answer if needed.
    answer = 0
    if incSum:
      if elements[1] == "+":
        answer = int(elements[0]) + int(elements[2])
      elif elements[1] == "-":
        answer = int(elements[0]) - int(elements[2])

    # Add 4 characters of whitespace if it is not the first problem.
    if index != 0:
      results[0] += "    "
      results[1] += "    "
      results[2] += "    "
      if incSum:
        results[3] += "    "

    # Get the length of the longest number and the whitespaces after the operator.
    num_one_longer = len(elements[0]) > len(elements[2])
    space_before_num_one = ""
    space_before_num_two = ""

    # If the first number is longer, get two spaces for behind it, then add the
    # difference minus 1 to the second number.
    if num_one_longer:
      space_before_num_one = generate_space(2)
      space_before_num_two = generate_space(
          len(elements[0]) - len(elements[2]) + 1)
    # Otherwise, get 1 space for behind the second number and get the difference for
    # the first one.
    else:
      space_before_num_two = generate_space(1)
      space_before_num_one = generate_space(
          len(elements[2]) - len(elements[0]) + 2)

    # Push the first line into the results.
    section_one = space_before_num_one + elements[0]
    results[0] += section_one

    # Push the second line into the results.
    section_two = elements[1] + space_before_num_two + elements[2]
    results[1] += section_two

    # Find which section is longer.
    sect_one_longer = len(section_one) > len(section_two)

    # If section one is longer, add a dash to the third line for each character from it.
    if sect_one_longer:
      for i in range(len(section_one)):
        results[2] = results[2] + "-"
    # Otherwise do it for section two instead.
    else:
      for i in range(len(section_two)):
        results[2] = results[2] + "-"

    # Get the space for before the answer
    # (length of longest number - length of answer + 2).
    space_before_answer = ""
    if num_one_longer:
      space_before_answer = generate_space(
          len(elements[0]) - len(str(answer)) + 2)
    else:
      space_before_answer = generate_space(
          len(elements[2]) - len(str(answer)) + 2)

    # Add the answer to the fourth line if needed.
    if incSum:
      results[3] += space_before_answer + str(answer)

  # Combine the results strings and return the final output.
  arranged_problems = "\n".join(results)
  return arranged_problems
