#!/usr/bin/bash
# Add packages from current directory to a given repository

readonly scriptname='addpkg'

# default options
declare -a files
declare -a opts
declare -a sigfiles
clean_cachedir=0
compression='xz'

# Error messages
readonly no_compression_entered='No compression type entered.'
readonly nosuchdir='No such directory'

printHelp() {
cat << EOF
Usage: ${scriptname} [options] [repository] -- [additional repo-add opts]
Options:
    -C, --compression-type      the compression algorithm the db is using
    -c, --clean-cachedir        use paccache to clean the cache directory
    -R, --remove                remove old package files
    -s, --sign                  sign repository file
EOF
}

while true; do
    case "${1}" in
        '-c'|'--clean-cachedir')
            clean_cachedir=1
            shift
            continue
            ;;
        '-C'|'--compression-type')
            case "${2}" in
                "")
                    printf '%s\n' "${no_compression_entered}" >&2
                    exit 1
                    ;;
                *)
                    compression="${2}"
                    ;;
            esac
            shift 2
            continue
            ;;
        --compression-type=*)
            compression="${1#*=}"
            [[ -z "${compression}" ]] &&\\
                printf '%s\n' "${no_compression_entered}" >&2 && exit 1
            shift
            continue
            ;;
        '-h'|'--help')
            printHelp
            exit 0
            ;;
        '-r'|'--remove')
            opts+=('--remove')
            shift
            continue
            ;;
        '-s'|'--sign')
            opts+=('--sign')
            shift
            continue
            ;;
        --)
            shift
            break
            ;;
        -*)
            printf '%s\n' "Unknown option: ${1}"
            exit 1
            ;;
        *)
            break
            ;;
    esac
done

repo="${1}" && shift
repo_dir="/var/cache/pacman/${repo}"
repo_db="${repo_dir}/${repo}.db.tar.${compression}"
extra_opts=("${@}")

[[ ! -d "${repo_dir}" ]] && printf '%s\n' "${repo_dir}: ${nosuchdir}" >&2

files=(*.pkg.tar.xz)
sigfiles=(*.pkg.tar.xz.sig)

# run repo-add before moving files
repo-add "${opts[@]}" "${extra_opts[@]}" "${repo_db}" "${files[@]}"

# move package files and sig files into repository directory
mv "${files[@]}" "${sigfiles[@]}" "${repo_dir}"

if [[ "${clean_cachedir}" == 1 ]]; then
    [[ ! -x '/usr/bin/paccache' ]] && echo 'paccache is not present, skipping'
    paccache --verbose --remove --keep 1 --cachedir "${repo_dir}"
fi
