#!/usr/bin/bash
# Fuzzy find a file and then check which package owns it

declare -r scriptname="fqo"

printHelp() {
cat << helpinfo
${scriptname} - fuzzy find a file and then check which package owns it

Usage: ${scriptname} [-h] [patterns]

Options:
    -h, --help  print this help page
helpinfo
}

while true; do
    case "${1}" in
        "-h"|"--help")
            printHelp
            exit
            ;;
        --)
            shift
            break
            ;;
        -*)
            printf '%s\n' "Unknown option: ${1}" >&2
            exit 1
            ;;
        *)
            break
            ;;
    esac
done

[[ ! -x '/usr/bin/locate' ]] && echo 'locate is not present' && exit 1
[[ ! -x '/usr/bin/fzf' ]] && echo 'fzf is not present' && exit 1
[[ -z "${*}" ]] && printf '%s\n' "No patterns entered" >&2 && exit 1

file="$(locate --all --ignore-case --null -- "${@}" | fzf --exit-0 --select-1 --read0 --no-mouse)"
[[ ! "${file}" ]] && exit 1

pacman -Qo "${file}"
