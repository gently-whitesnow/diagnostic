ARG SDK_VERSION=8.0
ARG RUNTIME_VERSION=8.0

FROM mcr.microsoft.com/dotnet/aspnet:${RUNTIME_VERSION} AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:${SDK_VERSION} AS sdk
WORKDIR /src
COPY ["Service.csproj", "./"]
RUN dotnet restore "Service.csproj"
COPY . .
WORKDIR "/src/"
RUN dotnet build "Service.csproj" -c Release -o /app/build

FROM sdk AS publish
RUN dotnet publish "Service.csproj" -c Release -o /app/publish /p:UseAppHost=false

FROM sdk as tools
ARG RUNTIME_VERSION
RUN dotnet tool install --version "${RUNTIME_VERSION}.*" --tool-path /tools dotnet-trace
RUN dotnet tool install --version "${RUNTIME_VERSION}.*" --tool-path /tools dotnet-counters
RUN dotnet tool install --version "${RUNTIME_VERSION}.*" --tool-path /tools dotnet-dump


FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
COPY --from=tools /tools /tools
ENTRYPOINT ["dotnet", "Service.dll"]
