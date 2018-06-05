import sys, getopt
vcf_header = '##fileformat=VCFv4.1\n##source=vcf_intersect.py\n#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n'
USAGE = 'USAGE: vcf_intersect.py -i "[file 1] [& or |] [file2] [& or |] [file 3] ..." -o [output_file]'
NOTE = 'NOTE:   This program only provides the most rudementary information about\n\
        the mutations, please refer back to the original VCFs to get more\n\
        information about the mutations. A great way to do this is to import\n\
        all your VCFs into IGV.'


def main(argv):
        print 'Hello World!'
        cmd = ''
        output = ''
        try:
                opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
        except getopt.GetoptError:
                print USAGE + '\n'
                print NOTE
                sys.exit(2)
        for opt, arg in opts:
                if opt in ('-h','--help'):
                        print USAGE + '\n'
                        print NOTE
                        sys.exit()
                elif opt in ('-i', '--input'):
                        cmd = arg
                elif opt in ('-o', '--output'):
                        output = arg
        print 'Command: %s' % cmd
        print 'Output file: %s' % output
        with open(output, 'w') as out:
                merge(cmd, out)

def merge(cmd, out):
        #splitting cmd up into a list of list of &
        cmd_list = cmd.split(' ')
        first_vcf = cmd_list.pop(0)
        isec_list = [[first_vcf]]
        while len(cmd_list) > 0:
                logic = cmd_list.pop(0)
                file = cmd_list.pop(0)
                if logic == '&':
                        isec_list[len(isec_list)-1].append(file)
                else:
                        isec_list.append([file])
        result = process_union(process_intersect(isec_list))
        out.write(vcf_header)
        for r in result:
                out.write(r + '\t.\t.\t.\n')

def getPosition(file):
        loc_list = []
        with open(file, 'r') as input:
                line = input.readline()
                while len(line) > 1:
                        if '#' not in line:
                                loc_list.append('\t'.join(line.split('\t')[:5]))
                        line = input.readline()
        return loc_list

def process_intersect(isec_list):
        intersects = []
        for files in isec_list:
                first = getPosition(files.pop())
                while len(files) > 0:
                        next = getPosition(files.pop())
                        first = list(set(first).intersection(next))
                intersects.append(first)
        return intersects

def process_union(intersects):
        first = intersects.pop()
        while len(intersects) > 0:
                first = list(set(first).union(intersects.pop()))
        return first

if __name__ == '__main__' :
        main(sys.argv[1:])
