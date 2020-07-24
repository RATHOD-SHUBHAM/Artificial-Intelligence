class PosteriorProbability():
    def __init__(self,observation):
        pofQueries = []
        p = 0
        pofQueries.append([0.1, 1.0, 0.0])
        pofQueries.append([0.2, 0.75, 0.25])
        pofQueries.append([0.4, 0.5, 0.5])
        pofQueries.append([0.2, 0.25, 0.75])
        pofQueries.append([0.1, 0.0, 1.0])
        outFile = 'result.txt'
        file = open(outFile, 'w')
        file.write("Observation sequence Q: %s\t\n" % observation)
        file.write("Length of Q: %s\n\n\n" % len(observation))

        def result(pOfNextQisC, candy):
            for i in range(0, 5):
                if candy == 'C':
                    pofQueries[i][0] = ((pofQueries[i][1] * pofQueries[i][0]) / pOfNextQisC)
                elif candy == 'L':
                    pofQueries[i][0] = ((pofQueries[i][2] * pofQueries[i][0]) / pOfNextQisC)

            #  local variable 'p' referenced before assignment
            nonlocal p
            p = p+1

            file.write("After Observation " + str(p) + " = " + str(candy) + ":\n\n")
            file.write("P(h1 | Q) = %.10f \n" % pofQueries[0][0])
            file.write("P(h2 | Q) = %.10f \n" % pofQueries[1][0])
            file.write("P(h3 | Q) = %.10f \n" % pofQueries[2][0])
            file.write("P(h4 | Q) = %.10f \n" % pofQueries[3][0])
            file.write("P(h5 | Q) = %.10f \n" % pofQueries[4][0])

            pOfNextQisC = 0.0
            pOfNextQiscL = 0.0

            for i in range(0, 5):
                pOfNextQisC += (pofQueries[i][0] * pofQueries[i][1])
                pOfNextQiscL += (pofQueries[i][0] * pofQueries[i][2])
            file.write("Probability that the next candy we pick will be C, given Q: %.10f \n" % pOfNextQisC)
            file.write("Probability that the next candy we pick will be L, given Q: %.10f \n\n" % pOfNextQiscL)


        if len(observation) == 0:
            file.write("P(h1 | Q) = %.10f \n" % pofQueries[0][0])
            file.write("P(h2 | Q) = %.10f \n" % pofQueries[1][0])
            file.write("P(h3 | Q) = %.10f \n" % pofQueries[2][0])
            file.write("P(h4 | Q) = %.10f \n" % pofQueries[3][0])
            file.write("P(h5 | Q) = %.10f \n" % pofQueries[4][0])
            file.write("Probability that the next candy we pick will be C, given Q: 0.50000\n")
            file.write("Probability that the next candy we pick will be L, given Q: 0.50000\n")
            file.close()
        else:
            for i in range(0, len(observation)):
                pOfNextQisC = 0.0
                pOfNextQiscL = 0.0

                for j in range(0, 5):
                    pOfNextQisC += (pofQueries[j][0] * pofQueries[j][1])
                    pOfNextQiscL += (pofQueries[j][0] * pofQueries[j][2])

                if observation[i] == 'C':
                    result(pOfNextQisC, 'C')
                elif observation[i] == 'L':
                    result(pOfNextQiscL, 'L')
                else:
                    print("Invalid")