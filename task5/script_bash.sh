RED='\e[31m'
GREEN='\e[32m'
RESET='\e[0m'

declare -i total_attempts=0
declare -i correct_attempts=0
declare -a game_history=()
declare -a result_history=()

while true; do
    secret_number=$((RANDOM % 10))

    echo "Step: $((total_attempts + 1))"
    read -p "Please enter number from 0 to 9 (q - quit): " user_input

    if [ "$user_input" == "q" ]; then
        echo "Game over. Thank you for playing!"
        break
    fi

    if [[ ! "$user_input" =~ ^[0-9]$ ]]; then
        echo "Error! Please enter a valid number from 0 to 9."
        continue
    fi

    total_attempts+=1
    game_history+=("$user_input")


    if [ "$user_input" -eq "$secret_number" ]; then
        correct_attempts+=1
        result_history+=("${GREEN}$secret_number${RESET}")
        echo -e "Hit! My number: $secret_number"
    else
        result_history+=("${RED}$secret_number${RESET}")
        echo -e "Miss! My number: $secret_number"
    fi

    hit_percentage=$((correct_attempts * 100 / total_attempts))
    miss_percentage=$((100 - hit_percentage))

    echo "Hit: $hit_percentage% Miss: $miss_percentage%"
    echo -n "Numbers: "

    num_to_display=${#result_history[@]}
    if [ "$num_to_display" -gt 10 ]; then
        num_to_display=10
    fi

    for ((i = ${#result_history[@]} - num_to_display; i < ${#result_history[@]}; i++)); do
        echo -n -e "${result_history[$i]} "
    done


    echo -e "\n"
done