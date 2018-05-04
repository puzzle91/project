import Currency
import Airport

def calculate_trip(self,code1,code2,code3,code4):


        
        depart_home = Airport
        airport_2 = Airport
        airport_3 = Airport
        airport_4 = Airport
        return_home = Airport

        depart_home=Airport.createInstance(depart_home,code1)
        airport_2=Airport.createInstance(airport_2,code2)
        airport_3=Airport.createInstance(airport_3,code3)
        airport_4=Airport.createInstance(airport_4,code4)
        return_home=Airport.createInstance(return_home,code1)
        
        #print("information on airport 1:",code1,airport_1,"\ninformation on airport 2:",code2,airport_2),"\ninformation on airport 3:",code3,airport_3,"\ninformation on airport 4:",code4,airport_4)

        lat1  = depart_home[1]
        long1 = depart_home[2]
        lat2  = airport_2[1]
        long2 = airport_2[2]
        first_trip=(self.calculate_distance(lat1, long1, lat2, long2))
        print ("first trip distance:",first_trip)
        

        lat2  = airport_2[1]
        long2 = airport_2[2]
        lat3 = airport_3[1]
        long3 = airport_3[2]

        second_trip=(self.calculate_distance(lat2, long2, lat3, long3))
        #print ("second trip distance:",second_trip)
        
        
        lat3  = airport_3[1]
        long3 = airport_3[2]
        lat4 = airport_4[1]
        long4 = airport_4[2]

        third_trip=(self.calculate_distance(lat3, long3, lat4, long4))
        #print ("third trip distance:",third_trip)

       

        lat4 = airport_4[1]
        long4 = airport_4[2]
        lat5 = return_home[1]
        long5= return_home[2]

        fourth_trip=(self.calculate_distance(lat4, long4, lat5, long5))
        #print ("fourth trip distance:",fourth_trip)

        final_distance = third_trip + second_trip +first_trip+fourth_trip
        #print("the final distance between airports is:",final_distance)

def possibleTrips(self,home, airport_2,airport_3,airport_4,airport_5):
        start_time=time.time()

        Code4 = input("Enter the fourth destination: ").upper()
        Home = input("Enter Home airport: ").upper()
        Code2 = input("Enter the destination airport: ").upper()
        Code3 = input("Enter the third destination airport: ").upper()
        Code4 = input("Enter the fourth destination: ").upper()

         #creates a list of tuples with all possible permutations:
        trips_possible_1 = list(itertools.permutations([home,airport_2,airport_3,airport_4,airport_5], 5))

        trips_possible_1 = [list(i) for i in trips_possible_1]
        #second trip
        trips_possible_2 = list(itertools.permutations([home,airport_2,airport_3,airport_4,airport_5], 5))

        trips_possible_2 = [list(i) for i in trips_possible_2]

        #third trip
        trips_possible_3 = list(itertools.permutations([home,airport_2,airport_3,airport_4,airport_5], 5))

        trips_possible_3 = [list(i) for i in trips_possible_3]

         #fourth trip
        trips_possible_4 = list(itertools.permutations([home,airport_2,airport_3,airport_4,airport_5], 5))

        trips_possible_4 = [list(i) for i in trips_possible_4]

         #fifth trip
        trips_possible_5 = list(itertools.permutations([home,airport_2,airport_3,airport_4,airport_5], 5))

        trips_possible_5 = [list(i) for i in trips_possible_5]

        #potential legs based on trips
        first_leg=list(trips_possible_1)

        second_leg = list(trips_possible_2)

        third_leg = list(trips_possible_3)

        fourth_leg = list(trips_possible_4)

        fifth_leg= list(trips_possible_5)


        #I assume that the airport has one main flight leg between two airports at close proximity and travels between them#
        main_leg = list(itertools.permutations([first_leg,second_leg,third_leg,fourth_leg,fifth_leg], 2))
        return("potential main leg:", main_leg)

        #print(fifth_leg)

        #make trips_possible into a full list:

        max_possible_permuations = list(fifth_leg + fourth_leg + third_leg +second_leg+first_leg)
        #return (max_possible_permuation)    

        #Change it from being a list of tuples into a list of lists where the ith element
        #  is the list inside the list(so we can calcuate leg journeys)

        for tuple_values in max_possible_permuations:
            tuple_values = list(tuple_values)
            #make it so we always leave from home
            list(tuple_values).insert(0,home)
            #make it so we always return to home
            tuple_values.insert(5,home)
            #print(tuple_values)
            #remove the last index since we inserted new index (and old 5->6)
            tuple_values.remove(tuple_values[6])
            #removes some duplicates

            

            #creating lists to store my trips later
            total_distance_list=[]   
            trips=[]
            total_cost={}
       
            pound = Currency
            dollar = Currency
            calculate = AirportAtlas("airport.csv")
            pound = Currency.FindConversion(currencyRate,'GBP')
            dollar = Currency.FindConversion(currencyRate,'USD')
        

            trip_1= calculate.getAirportDistance(tuple_values[0],tuple_values[1])
            print(trip_1)

            trip_1=float(trip_1)
            trips.append(trip_1)
            cost1=trip_1
            total_cost.update({'trip_1':cost1}) 
            #cost is in euro as it fuels in Dublin
            #print(trip_1)
           
      
            trip_2=calculate.getAirportDistance(tuple_values[1],tuple_values[2])

            trip_2=float(trip_2)
            trips.append(trip_2)
            cost2=trip_2*pound
            total_cost.update({'trip_2':cost1})
            #cost is in pounds as it fuelds in London


            trip_3=calculate.getAirportDistance(tuple_values[2],tuple_values[3])
            trip_3=float(trip_3)
            trips.append(trip_3)
            cost3=trip_3*dollar
            total_cost.update({'trip_3':cost3})
            #cost is in Dollars as it fuels in New york

            trip_4=calculate.getAirportDistance(tuple_values[3],tuple_values[4])
            trip_4=float(trip_4)
            trips.append(trip_4)
            cost4=trip_4*pound
            total_cost.update({'trip_4':cost4})
            #cost is in pounds as it fuels again back in london
    
            trip_5=calculate.getAirportDistance(tuple_values[4],tuple_values[0])
            trip_5=float(trip_5)
            trips.append(trip_5)
            cost5=int(trip_5)
            total_cost.update({'trip_5': cost5})
            #back in dublin

            all_triplist = trips[:]

            minimum_distance=min(all_triplist) #Min distance route is the optimum route for the 5 plane problem for is little currency
            # fluctuation between the airports/countries I am using (JFK, LHR, DUB, CDG) as Dublin also always occurs at least twice. 
            maximum_distance=max(all_triplist)

            print (total_cost)

            minimumCost = min(total_cost,key=total_cost.get)
            maximumCost = max (total_cost,key=total_cost.get)

            
            
            #print("minimum distance travelled for in between all trips:", minimum_distance)
            #print (""minimum cost paid for travelling between all trips:", minimum_cost)")
            #print("maximum distance travelled in between  all trips:", maximum_distance)
            #print("maximum cost paid for travelling between all trips:", maximum_cost
            trip_6 = calculate.getAirportDistance(tuple_values[4],tuple_values[2])
            trips.append(trip_6)

            newlist_with_6th = trips[:]
            newlist_with_6th.append(trip_6)
            cost6=trip_6 
            total_cost.update({'trip_6':6})
            #we assume it is still in Europe
            total_distance=float(trip_3+trip_2+trip_1+trip_5+trip_4+trip_6)
            #note total_distance==min(Airport.__fuel_required)

            #print("total_distance travelled for trips:")
            total_distance_list=[trip_3 + trip_2 +trip_1+trip_5+trip_4+trip_6]
            #print("total_dist_list:",total_distance_list)
            total_dist_list = newlist_with_6th[:]
            one=min(total_dist_list)
            #print(one)
            


            #creating a dictionary with final distance as key with all final tuples as my values because
            #it would be more efficient for value lookup 
            total_distance_dict = {}
            
            total_distance_dict[total_distance] = tuple_values

           
            #print(total_distance_dict)
           
            total_dist_list = list(total_distance)[:]
            #shortest_final_journey = min(list(total_dist_list))
            #longest_final_journey = max(list(total_dist_list))

            #print('shortest trips in km is:', shortest_final_journey,
            #"longes_final_trip in km is:", longest_final_journey)

            #return shortest_final_journey, longest_final_journey


            #completes in 214.secs
            #print (total_distance_dict)

            Cost_dict={}

            trip = Airport

               #total_cost=trip*Currency.FindConversion(currencyRate,trip.getName(trip))
            

            print(Cost_dict)


            #print(trips)
            #print(total_distance_list)

        
            #print("The minimum total trip:", min(total_distance_list))

            
            print("--- %s seconds ---" % (time.time() - start_time))
try:
            currencyRate= Currency 
            
            CurrencyRate.createInstance(currencyRate,'EU')
            #usd=currencyRate.FindConversion(currencyRate,tuple_values[1])
            #gbp=currencyRate.FindConversion(currencyRate,tuple_values[2])
            #euro=currencyRate.FindConversion(currencyRate,tuple_values[0])
            costs=np.array
            leg_dist=np.array
        

except NameError:
        pass

  
             
             
