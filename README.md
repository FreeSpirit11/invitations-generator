# Invitations Generator

Welcome to the Invitations Generator! This Python script automates the process of creating personalized invitation cards. It takes a starting letter template and a list of names, and generates individual invitation cards by replacing placeholders with the names provided.

## Requirements
- Python 3.x

## How to Use

1. Clone the repository: `git clone https://github.com/FreeSpirit11/invitations-generator.git`
2. Place your starting letter template in the `Input/Letters` folder as `starting_letter.txt`.
3. Create a text file with a list of names in the `Input/Names` folder as `invited_names.txt`.
4. Run the script to generate the personalized invitation cards: `python invitations_generator.py`
5. The generated invitation cards will be saved in the `Output/ReadyToSend` folder as individual text files.

Make sure to customize the starting letter template with the placeholder `[name]` to indicate where the names should be inserted.

## File Structure

- `PycharmProjects/24. Mail Merge/Input/Letters/starting_letter.txt`: The template file containing the starting letter with the placeholder `[name]`.
- `PycharmProjects/24. Mail Merge/Input/Names/invited_names.txt`: The text file containing the list of names.
- `PycharmProjects/24. Mail Merge/Output/ReadyToSend/invitation_card_[name].txt`: The generated invitation cards for each name, saved as individual text files.

## Acknowledgments

This project is inspired by the #100DaysOfCode challenge by Angela Yu.

Enjoy using the Invitations Generator to simplify your invitation card creation process!

